from thefuzz import fuzz, process
import pandas as pd

def search_all(df, query):
    
    scores = process.extract(
        query, 
        df['_concatenated'], 
        scorer=fuzz.partial_ratio,
        limit=5
    )
    
    ids = [ score[-1] for score in scores ]
        
    return df.iloc[ids]
    

def load_data():
    df = pd.read_csv('data.csv')
    # create column for fuzzy search
    df['_concatenated'] = pd.Series(df.astype(str).fillna('').values.tolist()).str.join(' ')
    return df

