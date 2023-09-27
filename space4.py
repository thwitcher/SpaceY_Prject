import folium
import wget
import pandas as pd
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon
from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


spacex_csv_file = open('spacex_launch_geo.csv','r+')
spacex_df=pd.read_csv(spacex_csv_file)
spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
launch_sites_dff = launch_sites_df[['Lat', 'Long']]
nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)
circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)
long, lat =[], []
long =launch_sites_dff['Long'].tolist()
lat = launch_sites_dff['Lat'].tolist()
for i in range(4):
    cord = [lat[i], long[i]]
    folium.Marker(cord).add_to(site_map)




marker_cluster = MarkerCluster()

def ClassColor(data):
    if int(data[0]) == 1 :
        return 'green'
    else:
        return 'red'
lyss =[]
for i,j in spacex_df.iterrows() :
    lyss.append(ClassColor(j[['class']]))
    
spacex_df['Color'] = lyss

site_map.add_child(marker_cluster)

for index, record in spacex_df.iterrows():
    lat = record['Lat']
    lon = record['Long']
    color = record['Color']

    marker = folium.Circle([lat, lon], radius=1000, color=color, fill=True)
    
    marker.add_to(marker_cluster)


formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    separator=' Long: ',
    empty_string='NaN',
    lng_first=False,
    num_digits=20,
    prefix='Lat:',
    lat_formatter=formatter,
    lng_formatter=formatter,
)

site_map.add_child(mouse_position)
laS1 = 34.63368
loS1 = -120.61391

laS1_0 = 34.63691
loS1_0 = -120.62349

laS1_1 = 34.63716
loS1_1 = -120.62452

laS1_2 = 34.87998
loS1_2 = -120.49427

laS1_3 = 34.94546
loS1_3 = -120.44174

dist0 = calculate_distance(laS1, loS1, laS1_0, loS1_0)

dist1 = calculate_distance(laS1, loS1, laS1_1, loS1_1)

dist2 = calculate_distance(laS1, loS1, laS1_2, loS1_2)

dist3 = calculate_distance(laS1, loS1, laS1_3, loS1_3)

istance_marker = folium.Marker(
    [laS1_0 , loS1_0],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(dist0),
        )
   )

polyline_coordinates = [(laS1, loS1),(laS1_0, loS1_0)]
polyline = folium.PolyLine(locations=polyline_coordinates, color='black')
polyline.add_to(site_map)
site_map.add_child(istance_marker)

istance_marker1 = folium.Marker(
    [laS1_1 , loS1_1],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 22; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(dist1),
        )
   )

polyline_coordinates1 = [(laS1, loS1),(laS1_1, loS1_1)]
polyline1 = folium.PolyLine(locations=polyline_coordinates1, color='black')
polyline1.add_to(site_map)
site_map.add_child(istance_marker1)

istance_marker2 = folium.Marker(
    [laS1_2 , loS1_2],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 22; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(dist2),
        )
   )

polyline_coordinates2 = [(laS1, loS1),(laS1_2, loS1_2)]
polyline2 = folium.PolyLine(locations=polyline_coordinates2, color='black')
polyline2.add_to(site_map)
site_map.add_child(istance_marker2)

istance_marker3 = folium.Marker(
    [laS1_3 , loS1_3],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 22; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(dist3),
        )
   )

polyline_coordinates3 = [(laS1, loS1),(laS1_3, loS1_3)]
polyline3 = folium.PolyLine(locations=polyline_coordinates3, color='black')
polyline3.add_to(site_map)
site_map.add_child(istance_marker3)







site_map.save('my_map.html')

