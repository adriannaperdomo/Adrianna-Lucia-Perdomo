import googlemaps
from datetime import datetime


gmaps = https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


import (/data/{index}/attributes/wheelchair_boarding)  
mbta = https://api-v3.mbta.com/docs/swagger/swagger.json
stop_name = directions_result
wheelchair acessible = using_wheelchair(directions_result)


import urllib.request
import json
from pprintimport pprint


YOUR_API_KEY = 'gmaps'
address = 'geocode_result'
url = f'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY'


f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)


for gmaps in ['geocode_result']:
    pprint.pprint(response_data['directions_result'])
    pprint.pprint(using_wheelchair)
        if using_wheelchair = 0, print('Infomration not Available')
        if using_wheelchair = 1, print('Wheelchair Acessible')
        if using_wheelchair = 2, print('No Wheelchair Access')
    print('The nearest MBTA stop is' stop_name['directions_result'])
    print('Wheelchair Access:' using_wheelchair['directions_result'])
                                     
pip install Flask
