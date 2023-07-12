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

def facility_map(filepath):
    
    # Utilizing plotly.express, map out the locations with lat/lon data by test frequencies.
    test_frequencies = df['Facility Name'].value_counts()
    # Once counted values per item, give the match items the same outcomes for mapbox.
    df['Frequencies'] = df['Facility Name'].map(test_frequencies)
    # Reason for the sorted_df is to configure the legend items by the size.
    sorted_df = df.sort_values(by='Frequencies', ascending=False)
    # Create the scatter map plot
    map_fig2 = px.scatter_mapbox(sorted_df, lat='Facility Latitude', lon='Facility Longitude',
                                color='Facility Name', size='Frequencies',
                                zoom=6, center={'lat': 39.17180415583127, 'lon': 126.551952046587},
                                width=1200, height=700, title='DPRK Missile Facility Locations')
    # Configure the text and layout
    map_fig2.update_layout(mapbox_style="carto-positron", title_font_size=25, title_font_family="Courier New")
    map_fig2.update_layout(margin_autoexpand=True)
    # Modify the legend position
    map_fig2.update_layout(title=dict(x=0.5, xanchor='center'))
    map_fig2.update_layout(margin=dict(t=45, l=0, r=0, b=5))
    # Display the scatter map plot
    map_fig2.show()
    

if __name__ == "__main__":
    df = import_file.load_file('data/north_korea_missile_test_database.csv')
    print(df.head(2))
    
    facility_map(df)