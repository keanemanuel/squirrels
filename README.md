CONTRIBUTORS
  Eiyrea Nabilla binti Azmi        eiyreanabillabinti.azmi@student.unimelb.edu.au
  Farrell Aurelio William          farrellaurelio.william@student.unimelb.edu.au
  Farah Aulia Zahra Irawan         firawan@student.unimelb.edu.au
  Keane Manuel                     keane.manuel@student.unimelb.edu.au

RESEARCH QUESTION
  Which behavioural and environmental factors are most strongly associated with
  squirrel approaches toward humans in Central Park, and can we reliably predict
  this behaviour?

================================================================================
FILES
================================================================================

  A2_Squirrel_Analysis_v4.ipynb   Main analysis notebook
  README.txt                      This file

  Required data files (place in the same folder as the notebook):
  squirrel.csv                    3,023 squirrel sighting records (31 variables)
  hectare.csv                     700 hectare-level environmental records
  stories.csv                     809 qualitative field notes (loaded but unused)

================================================================================
SETUP
================================================================================

Python 3.9 or above is required. Install all dependencies with:

  pip install pandas numpy matplotlib seaborn scikit-learn scipy

No additional configuration is needed.

================================================================================
HOW TO RUN
================================================================================

1. Place all files (notebook + three CSVs) in the same folder.

2. Launch Jupyter:
     jupyter notebook    or    jupyter lab

3. Open A2_Squirrel_Analysis_v4.ipynb.

4. Run all cells in order (Kernel > Restart & Run All).
   Do NOT run cells out of order — later cells depend on earlier ones.

Expected runtime: 5–20 seconds.

================================================================================
NOTEBOOK STRUCTURE
================================================================================

  Section 0   Imports and library setup
  Section 1   Load data
  Section 2   Exploratory Data Analysis (EDA)
  Section 3   Preprocessing
              3.1  Column removal
              3.2  Data validation
              3.3  Missing value imputation (mode)
              3.4  Feature engineering (Activity, Vocal, Human Interaction scores)
              3.5  Data integration (merge with hectare.csv)
              3.6  Categorical encoding (LabelEncoder)
              3.7  Class imbalance handling (stratified undersampling)
              3.8  Final feature matrix preparation
              3.9  Preprocessing impact comparison (Table 1)
  Section 4   Correlation Analysis
              4.1  Pearson correlation with target
              4.2  NMI with discretisation
              4.3  Pearson vs NMI comparison
              4.4  Behaviour correlation heatmap
              4.5  Behaviour rates by Approaches status
  Section 5   Supervised Learning
              5.1  Train/test split
              5.2  Decision Tree (criterion=entropy, max_depth=5)
              5.3  KNN (k selected via Pipeline CV, k=20)
              5.4  Confusion matrices
              5.5  Cross-validation comparison
              5.6  Feature importance (Decision Tree)
  Section 6   Clustering
              6.1  Feature preparation and normalisation
              6.2  Elbow method (k selection)
              6.3  KMeans (k=4)
              6.4  Hierarchical Clustering (Ward linkage)
              6.5  Cluster profiling
              6.6  PCA 2D visualisation
              6.7  Approach rate per cluster
              6.8  Silhouette score evaluation
              6.9  Cluster naming and interpretation
  Section 7   Summary table

================================================================================
OUTPUTS
================================================================================

All figures are saved as .png files in the notebook directory.

  EDA
    eda_behaviour_rates.png         Figure 1  — behaviour occurrence rates
    eda_categorical.png             Figure 2  — fur colour, shift, age distributions
    eda_spatial.png                 Figure 3  — spatial distribution by Approaches

  Preprocessing
    preprocessing_impact.png        Figure 4  — imbalance handling comparison

  Correlation
    correlation_with_target.png     Figure 5  — Pearson bar chart
    nmi_with_target.png             Figure 6  — NMI bar chart
    correlation_heatmap.png         Figure 7  — behaviour heatmap
    behaviour_by_approach.png       Figure 18 — behaviour rates by Approaches status

  Supervised Learning
    confusion_matrices.png          Figure 8  — DT and KNN confusion matrices
    decision_tree_viz.png           Figure 9  — DT visualisation (top 3 levels)
    knn_k_selection.png             Figure 10 — KNN k selection curve
    feature_importance_dt.png       Figure 11 — top 15 DT feature importances

  Clustering
    elbow_plot.png                  Figure 12 — elbow method
    silhouette_scores.png           Figure 13 — silhouette score vs k
    dendrogram.png                  Figure 14 — HC dendrogram (Ward, n=200)
    cluster_profiles.png            Figure 15 — normalised cluster profile bar chart
    cluster_pca.png                 Figure 16 — PCA 2D projection
    approach_by_cluster.png         Figure 17 — approach rate per cluster

All printed numerical results correspond directly to values reported in
A2_Report_Final.pdf.

================================================================================
NOTES
================================================================================

  - Data file path is configurable via the DATA_DIR variable at the top of
    Section 1 (default: '.', same folder as the notebook).
  - All random operations use random_state=42 for reproducibility.
  - Clustering runs on the full dataset (n=3,023), not the balanced subset,
    to capture the full range of behavioural variation.
  - The KNN Pipeline ensures scaling is fitted only on training data within
    each CV fold, preventing data leakage.
  - stories.csv is loaded but not used in the analysis. It is included for
    completeness and potential future use.

================================================================================
