import folium
map=folium.Map(location=[38.58, -99.09], zoom_start=6)
fg=folium.FeatureGroup(name="My Map")
for coordinates in [[38.52, -99.1],[35.52, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="hi i am marker", icon=folium.Icon(colour='green')))
map.add_child(fg)
map.save("Map1.html")
