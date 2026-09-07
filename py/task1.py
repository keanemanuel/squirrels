import pandas as pd

def task1():
    df = pd.read_csv("/course/squirrel.csv")
  
    # 1.1 Find the mode and fill missing ages with Mode
    if 'Age' in df.columns: 
        age_mode = df['Age'].mode()[0]
        df['Age'] = df['Age'].fillna(age_mode)


    # 1.2 One-Hot Encoding using Pandas (get_dummies) function
    if 'Primary Fur Color' in df.columns: # Primary Fur stores ONLY MAX 1 value
        primary = pd.get_dummies(df['Primary Fur Color'], prefix = 'Primary').astype(int) # pd.get_dummies gives boolean -> convert (int)
    else:
        primary = pd.DataFrame() # creates an empty table instead (REQUIRED FOR CONCAT)
    
    if 'Highlight Fur Color' in df.columns: # Highlight Fur stores 1..n multiple values
        df['Highlight Fur Color'] = df['Highlight Fur Color'].str.strip().fillna('') # Fill with '' instead because str.get_dummies() CANNOT handle NaN
        highlight = df['Highlight Fur Color'].str.get_dummies(sep = ',')
        highlight.columns = [f'Highlight_{column_title.strip()}'
        for column_title in highlight.columns] # Rename to prefix "Highlight"
    else:
        highlight = pd.DataFrame() # creates an empty table instead (REQUIRED FOR CONCAT)
    df = pd.concat([df, primary, highlight], axis=1)


    # 1.3 Regular Expressions (RegEx) on HectareSN and HectareWE
    if 'Hectare' in df.columns:
        # extract number and subtract 1 to get 0-41
        df['HectareSN'] = df['Hectare'].str.extract(r'(\d+)')
        df['HectareSN'] = pd.to_numeric(df['HectareSN'], errors = 'coerce') - 1
        # 'coerce' changes unextractable values to NaN, -1 to shift down 1 -> 0 and 42 -> 41

        # extract letter and map A=0, B=1 ... I=8
        df['HectareWE'] = df['Hectare'].str.extract(r'([A-I])')
        mapping = {chr(i+65): i for i in range(9)} # Converts to ASCII capitals A-I
        df['HectareWE'] = df['HectareWE'].map(mapping) 


    # Format to CSV 
    df.to_csv('task1_squirrel.csv', index = False) # avoids indexes[0,1,2,..]
    return df

    # print(df.columns)

    # Task 1.1 Check
    # print(df['Age'])

    # Task 1.2 Check
    # print(df[['Unique Squirrel ID',
    #           'Primary Fur Color',
    #           'Primary_Gray',
    #           'Primary_Cinnamon',
    #           'Primary_Black']].head(10)) 
    
    # print(df[['Unique Squirrel ID',
    #           'Highlight Fur Color',
    #           'Highlight_Gray',
    #           'Highlight_Cinnamon',
    #           'Highlight_Black']].head(10)) 
    
    # Task 1.3 Check
    # print(df[['Hectare','HectareSN','HectareWE']].loc[82])
    # print(df[['Hectare','HectareSN','HectareWE']].head(10))
    
