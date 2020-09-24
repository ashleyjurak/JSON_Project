import json

eseptinfile = open('US_fires_9_14.json', 'r')

eseptoutfile = open('esept_fire_data.json', 'w')

eseptdata = json.load(eseptinfile)

json.dump(eseptdata, eseptoutfile, indent = 4)

list_of_efires = eseptdata[]

elons, elats, ebrightness = [], [], []

for x in list_of_efires:
    lon = eq['longitude']
    lat = eq['latitude']
    bright = eq['brightness']
    elons.append(lon)
    elats.append(lat)
    ebrightness.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type' : 'scattergeo',
    'lon' : elons,
    'lat' : elats,
    'marker' : {
        'size' : [5 * bright for bright in ebrightness],
        'color' : ebrightness,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'}
    },
}]

my_layout = Layout(title = 'Fires')

fig = {'data' : data, 'layout' : my_layout}

offline.plot(fig, filename = 'end_sept_fires.html')