import numpy as np
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import descartes
import calendar
import seaborn as sns
import matplotlib

def load_file(filepath):
    df = pd.read_csv(filepath, encoding= 'unicode_escape', index_col= "F1")
    
    df['Distance Travelled'] = df['Distance Travelled'].apply(lambda x: x.replace('km', '') if isinstance(x, str) else x)
    # And then, convert 'Unkown' values to numerics.
    df['Distance Travelled'] = df['Distance Travelled'].replace('Unknown', 'NaN') 
    # Finally, I can change it to numeric pandas table.
    df['Distance Travelled'] = pd.to_numeric(df['Distance Travelled'], errors='coerce').fillna(0)
    df['Landing Location'] = df['Landing Location'].apply(lambda x: x.replace('330km east of Hachinohe and 4000 km out into Pacific Ocean', '330km east of Hachinohe') if isinstance(x, str) else x)
    # Changing 'location' data
    df['Facility Latitude'] = pd.to_numeric(df['Facility Latitude'], errors='coerce')
    df['Facility Longitude'] = pd.to_numeric(df['Facility Longitude'], errors='coerce')
    # Date changes
    df['Date'] = pd.to_datetime(df['Date'])
    # Creating a new column for separating the year values in numeric format.
    df['Year'] = df['Date'].dt.year
    # Another column for changing number values to string values.
    df['Month_Number'] = df['Date'].dt.month
    # Another column for separating values to month specifically.
    df['Month'] = df['Month_Number'].apply(lambda x: calendar.month_abbr[x])
    # Another column for counting test numbers.
    df["# of Test"] = 1
    # Simplifying the Year/Month format.
    df['YYYYMM'] = pd.to_datetime(df['Date'], format='%Y%m', errors='coerce')
    df['YYYYMM'] = pd.to_datetime(df['Date']).dt.strftime('%Y%m')
    
    return df

if __name__ == "__main__":
    my_df = load_file('data/north_korea_missile_test_database.csv')
    print(my_df.head(2))
    