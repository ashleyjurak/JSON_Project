import json

bseptinfile = open('US_fires_9_1.json', 'r')

bseptoutfile = open('bsept_fire_data.json', 'w')

bseptdata = json.load(bseptinfile)

json.dump(bseptdata, bseptoutfile, indent = 4)

list_of_bfires = bseptdata[]

blons, blats, bbrightness = [], [], []

for x in list_of_bfires:
    lon = eq['longitude']
    lat = eq['latitude']
    bright = eq['brightness']
    blons.append(lon)
    blats.append(lat)
    bbrightness.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type' : 'scattergeo',
    'lon' : blons,
    'lat' : blats,
    'marker' : {
        'size' : [5 * bright for bright in bbrightness],
        'color' : bbrightness,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'}
    },
}]

my_layout = Layout(title = 'Fires')

fig = {'data' : data, 'layout' : my_layout}

offline.plot(fig, filename = 'beg_sept_fires.html')