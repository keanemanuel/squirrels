import pandas as pd
import matplotlib.pyplot as plt
import re

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer

def remove_stop_words(text):
    # Step 3: remove stop words
    if isinstance(text, str):
        words = text.split()
        words = [w for w in words if w not in ENGLISH_STOP_WORDS]
        return ' '.join(words)
    return text

def apply_bow(df):
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(df['Specific Location'].dropna())
    return vectorizer, bow_matrix

def clean_text(df):
    # Step 1: LowerCase Letters
    if 'Specific Location' in df.columns:
        df['Specific Location'] = df['Specific Location'].str.lower()
    
    # Step 2: remove punctuation
        df['Specific Location'] = df['Specific Location'].apply(
            lambda x: re.sub(r'[^\w\s]', '', x) if isinstance(x, str) else x
        ) # checks if x is string, then implements the punctuation remove_stop_words
          # re.sub(pattern, replace, text)
          # re.sub(find patterns that are not characters/not spaces, replace with '', on string x)
    
    # Step 3: remove stop words
        df['Specific Location'] = df['Specific Location'].apply(remove_stop_words)
    return df

def extract_day_of_week(df):
    if 'Date' in df.columns:
        # Step 1: convert to string
        df['Date'] = df['Date'].astype(str)
        
        # Step 2: extract month, day, year using regex to create new date DataFrame
        date_parts = df['Date'].str.extract(r'(\d{2})(\d{2})(\d{4})')
        date_parts.columns = ['month', 'day', 'year']
        
        # Step 3: convert to date and get day name
        df['DAY_OF_WEEK'] = pd.to_datetime(date_parts).dt.day_name()
        # first changes to datetime format with hours 00:00:00 then changes to day name
    return df

def plot_days(df):
    day_counts = df['DAY_OF_WEEK'].value_counts()
    
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_counts = day_counts.reindex([d for d in day_order if d in day_counts.index])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    day_counts.plot(kind='bar', ax=ax)
    
    ax.set_title('Number of Squirrels Seen per Day of Week')
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('task3_days.png')
    plt.close()

def plot_wordpies(df):
    import numpy as np
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Step 1: find days that have data
    valid_days = [d for d in day_order 
                  if len(df[df['DAY_OF_WEEK'] == d]['Specific Location'].dropna()) > 0]
    
    # Step 2: create canvas - enough subplots for valid days
    n_days = len(valid_days)
    fig, axes = plt.subplots(1, n_days, figsize=(24, 12))
    axes = axes.flatten()  # convert 2D array to 1D for easy indexing
    
    # Step 3: draw one pie per day
    for i, day in enumerate(valid_days):
        # get top 5 words for this day
        day_df = df[df['DAY_OF_WEEK'] == day]['Specific Location'].dropna()
        vectorizer = CountVectorizer()
        bow = vectorizer.fit_transform(day_df)
        word_counts = np.array(bow.sum(axis=0)).flatten()
        words = vectorizer.get_feature_names_out()
        top5 = pd.Series(word_counts, index=words).sort_values(ascending=False).head(5)
        
        # draw pie
        axes[i].pie(top5, labels=top5.index, autopct='%1.1f%%')
        axes[i].set_title(day)
    
    # Step 4: hide unused axes
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)
    
    plt.suptitle('Top 5 Location Words per Day of Week')
    plt.tight_layout()
    plt.savefig('task3_wordpies.png')
    plt.close()

def plot_shifts(df):
    # Step 1: filter Monday, Friday, Sunday only
    filtered = df[df['DAY_OF_WEEK'].isin(['Monday', 'Friday', 'Sunday'])]
    
    # Step 2: group by day and shift
    grouped = filtered.groupby(['DAY_OF_WEEK', 'Shift']).size().unstack()
    
    # Step 3: reorder days
    grouped = grouped.reindex(['Monday', 'Friday', 'Sunday'])
    
    # Step 4: plot stacked bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    grouped.plot(kind='bar', stacked=True, ax=ax)
    
    # Step 5: labels
    ax.set_title('Number of Squirrels per Shift for Monday, Friday and Sunday')
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('Count')
    plt.xticks(rotation=0)
    
    plt.tight_layout()
    plt.savefig('task3_shifts.png')
    plt.close()

def task3():
    df = pd.read_csv('/course/squirrel.csv')
    
    # clean specific location
    df = clean_text(df)
    
    # extract day of week
    df = extract_day_of_week(df)
    
    # apply bag of words
    vectorizer, bow_matrix = apply_bow(df)

    #Plot 1, Plot 2, Plot 3
    plot_days(df) 
    plot_wordpies(df)      
    plot_shifts(df)  
