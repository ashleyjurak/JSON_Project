import json

eseptinfile = open('US_fires_9_14.json', 'r')

eseptoutfile = open('esept_fire_data.json', 'w')

eseptdata = json.load(eseptinfile)

json.dump(eseptdata, eseptoutfile, indent = 4)

elons, elats, ebrightness = [], [], []

for x in eseptdata:
    lon = x['longitude']
    lat = x['latitude']
    bright = x['brightness']
    elons.append(lon)
    elats.append(lat)
    if bright > 450:
        ebrightness.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type' : 'scattergeo',
    'lon' : elons,
    'lat' : elats,
    'marker' : {
        'size' : [.05 * bright for bright in ebrightness],
        'color' : ebrightness,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'}
    },
}]

my_layout = Layout(title = 'US Fires 9-14-20 to 9-20-2')

fig = {'data' : data, 'layout' : my_layout}

offline.plot(fig, filename = 'end_sept_fires.html')