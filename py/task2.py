import pandas as pd
import matplotlib.pyplot as plt
from task1 import task1

def task2():
    df = task1()  

    # Bar Chart
    grouped_df = df.groupby(['Shift', 'Primary Fur Color']).size().unstack(fill_value = 0) 
    # replaces NaN with 0
    # size -> tells the number of each group, unstack moves the attributes as columns

    fig, ax = plt.subplots(figsize=(10,8)) # Set size
    grouped_df.plot(kind='bar', ax=ax)     # ax=ax draws on our ax we defined along with the size

    ax.set_title('Distribution of Primary Fur Color across Shifts')
    ax.set_xlabel('Shift')
    ax.set_ylabel('Count')
    ax.legend(title='Primary Fur Color')
    plt.xticks(rotation=0) # x-axis labels to not rotate

    plt.savefig('task2_shift.png')
    plt.close()

    # Pie Chart
    eating_df = df[df['Eating'] == True]
    not_eating_df = df[df['Eating'] == False]

    eating_counts = eating_df['Primary Fur Color'].value_counts()
    not_eating_counts = not_eating_df['Primary Fur Color'].value_counts()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # draw pies
    # ax.pie(data_values, data_labels, percentages)
    ax1.pie(eating_counts, labels=eating_counts.index, autopct='%1.1f%%') 
    ax1.set_title('Primary Fur Color | Eating')

    ax2.pie(not_eating_counts, labels=not_eating_counts.index, autopct='%1.1f%%')
    ax2.set_title('Primary Fur Color | Not Eating')

    # save
    plt.savefig('task2_eating.png')
    plt.close()
