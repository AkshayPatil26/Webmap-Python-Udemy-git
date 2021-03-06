"""
adding multiple DYNAMIC POPUP markers from data file lec 78
"""


import pandas
import folium


data = pandas.read_csv("Volcanoes.txt")#reads csvfile in the folder

#conversion of LAT,LON column into list from the data
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#map.add_child(folium.Marker(location=[80.01,-100.01],popup="This is test marker", icon=folium.Icon(color='green')))

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[44,-120], zoom_start=4) #creates map

#creates map object for marker
fg = folium.FeatureGroup(name="My Map")

#for loop for multiplecoordinates as list
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el)+" m", radius=10, fill_opacity=0.6, fill_color=color_producer(el), color=color_producer(el)))
    map.add_child(fg)
    #CircleMarker with parameters radius, fill_color, color, fill_opacity
    #popup accepts only string characters
    #changed from icon=folium.Icon(color=color_producer(el))

map.save("maptest6.html")
