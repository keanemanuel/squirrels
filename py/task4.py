import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import gaussian_kde


def encode_boolean(value):
    if pd.isna(value):
        return 0

    value_str = str(value).strip().lower()

    if value_str in ['true', '1', 'yes']:
        return 1
    if value_str in ['false', '0', 'no', 'nan', '']:
        return 0

    return 0


def extract_date_numeric(date_value):
    if pd.isna(date_value):
        return np.nan

    match = re.fullmatch(r'(\d{2})(\d{2})(\d{4})', str(date_value).strip())
    if not match:
        return np.nan

    month, day, year = match.groups()

    try:
        dt = pd.Timestamp(year=int(year), month=int(month), day=int(day))
        return dt.toordinal()
    except ValueError:
        return np.nan


def prepare_features(df):
    sighting_features = [
        'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging',
        'Kuks', 'Quaas', 'Moans',
        'Tail flags', 'Tail twitches',
        'Approaches', 'Indifferent', 'Runs from'
    ]

    df = df.copy()

    for col in sighting_features:
        df[col] = df[col].apply(encode_boolean)

    df['Date_num'] = df['Date'].apply(extract_date_numeric)

    feature_cols = sighting_features + ['Date_num', 'X', 'Y']

    df = df.dropna(subset=feature_cols).copy()

    scaler = MinMaxScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    return df, feature_cols


def plot_elbow(X):
    distortions = []
    k_range = range(1, 11)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(k_range, distortions, 'bx-')
    plt.title('The Elbow Method showing the optimal k')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.xticks(range(1, 11))
    plt.tight_layout()
    plt.savefig('task4_elbow.png')
    plt.close()


def run_kmeans(X, k):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    return kmeans, labels


def plot_scatter(original_df, labels):
    plt.figure(figsize=(8, 6))
    plt.scatter(original_df['X'], original_df['Y'], c=labels, s=12, cmap='tab10')
    plt.title('K-Means Clustering')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.tight_layout()
    plt.savefig('task4_scatter.png')
    plt.close()


def save_clusters(processed_df, original_df, labels, kmeans, feature_cols):
    processed_df = processed_df.copy()
    processed_df['cluster'] = labels

    for cluster_id in range(kmeans.n_clusters):
        cluster_rows = processed_df[processed_df['cluster'] == cluster_id].copy()

        center = kmeans.cluster_centers_[cluster_id]
        distances = np.linalg.norm(cluster_rows[feature_cols].values - center, axis=1)
        cluster_rows['distance'] = distances

        top_indices = cluster_rows.sort_values('distance').head(10).index
        output_df = original_df.loc[top_indices]

        output_df.to_csv(f'task4_cluster{cluster_id}.csv', index=False)


def plot_density(original_df):
    x = original_df['X'].dropna().to_numpy()
    y = original_df['Y'].dropna().to_numpy()

    img = plt.imread('/course/centralpark.png')

    xmin = -73.992919921875
    xmax = -73.948974609375
    ymin = 40.75557964275589
    ymax = 40.805493843894155

    kde = gaussian_kde(np.vstack([x, y]))

    xi, yi = np.meshgrid(
        np.linspace(xmin, xmax, 200),
        np.linspace(ymin, ymax, 200)
    )

    positions = np.vstack([xi.ravel(), yi.ravel()])
    zi = kde(positions).reshape(xi.shape)

    plt.figure(figsize=(8, 8))
    plt.imshow(
        img,
        extent=[xmin, xmax, ymin, ymax],
        origin='upper',
        aspect='auto'
    )

    plt.contourf(xi, yi, zi, levels=20, cmap='Reds', alpha=0.45)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Squirrel Density')
    plt.tight_layout()
    plt.savefig('task4_density.png')
    plt.close()


def task4():
    df = pd.read_csv('/course/squirrel.csv')

    df = df.dropna(subset=['X', 'Y']).copy()
    original_df = df.copy()

    processed_df, feature_cols = prepare_features(df)
    original_df = original_df.loc[processed_df.index].copy()

    X = processed_df[feature_cols]

    plot_elbow(X)

    # choose k from visual inspection of elbow plot
    k = 3

    kmeans, labels = run_kmeans(X, k)

    plot_scatter(original_df, labels)
    save_clusters(processed_df, original_df, labels, kmeans, feature_cols)
    plot_density(original_df)
