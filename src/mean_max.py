import import_file
import numpy as np
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import descartes
import calendar
import seaborn as sns
import matplotlib

def mean_max(filepath):
    df = import_file.load_file('data/north_korea_missile_test_database.csv')
    # This chart requires two different values (max & mean). Therefore, the following lines defines both max range and mean range
    df_distance = df[['Year','Distance Travelled']]
    grouped_distance = df_distance.groupby('Year')
    df_range_max = grouped_distance.max().reset_index()
    df_range_max = df_range_max.dropna()
    df_range_max.rename(columns = {"Distance Travelled": "Reach (km)"}, inplace=True)
    df_range_max['Category'] = "Maximum"
    # Here starts the mean range
    df_distance = df[['Year','Distance Travelled']]
    grouped_distance = df_distance.groupby('Year')
    df_range_mean = grouped_distance.mean().reset_index()
    df_range_mean = df_range_mean.dropna()
    df_range_mean.rename(columns = {"Distance Travelled": "Reach (km)"}, inplace=True)
    df_range_mean['Category'] = "Average"
    # Now, concatenate two data (max & mean) to blend two data in a same bar
    df_reach = pd.concat([df_range_mean,df_range_max])
    df_reach = df_reach[df_reach['Reach (km)'] != 0.0]
    # Configuration
    fig = plt.figure(figsize=(18, 10))
    ax1 = sns.set_theme(style="white")
    ax1 = plt.gca().spines['left'].set_color('black')
    ax1 = plt.gca().spines['bottom'].set_color('black')
    plt.title('DPRK missile traveled distance expansions by timeline', fontsize = 16, loc='center')
    # Creating a plot
    ax1 = sns.barplot(x='Reach (km)', y='Year', hue="Category", data=df_reach, orient="h", palette="colorblind")
    # Setting the tick marks
    xticks = np.arange(0, df_reach['Reach (km)'].max()+250, 250)
    
    plt.show()
    return

if __name__ == "__main__":
    df = import_file.load_file('data/north_korea_missile_test_database.csv')
      
    mean_max(df)
