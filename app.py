import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data
data = pd.DataFrame({
    'City': ['Los Angeles', 'New York', 'Chicago'],
    'Latitude': [34.0522, 40.7128, 41.8781],
    'Longitude': [-118.2437, -74.0060, -87.6298]
})

# Streamlit app layout
st.title('Simple Streamlit Dashboard')

# Display DataFrame
st.write("### Sample Data")
st.write(data)

# Create a simple map
st.write("### Map Visualization")
map_ = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Centered on the USA

# Add markers to the map
for index, row in data.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['City']).add_to(map_)

# Display the map in Streamlit
st_folium(map_, width=700, height=500)
