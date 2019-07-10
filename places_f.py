import requests
import numpy as np
import json
import os

#retreive info from Sygic travel site

X = os.environ.get('X-API-KEY')


headers = headers = {"x-api-key ": X
          }

def location_id(location):
    url_place = 'https://api.sygictravelapi.com/1.1/en/places/list?limit=1&query='+location
    global headers 
    city_id = requests.get(url_place,headers=headers)
    x = json.loads(city_id.content)
    city_id = x.get('data').get('places')[0].get('id')
    country_id = list(filter(lambda x: x[0:7] == 'country',x.get('data').get('places')[0].get('parent_ids')))
    return city_id, country_id[0]

def places(place_id):    
    
    url_collection = 'https://api.sygictravelapi.com/1.1/en/collections'
    global headers
    newlist = {'sightseeing': [], 'hiking': [],'eating':[],'discovering': [], 'going_out': [],'playing':[],'relaxing': [], 
           'shopping': [],'sleeping':[],'doing_sports': [], 'traveling': []}
    params = {'parent_place_id': place_id}
    req_collection = requests.get(url_collection,headers=headers,params = params)
    x = json.loads(req_collection.content)
    y = x.get('data').get('collections')[0].get('place_ids')
    for i in y:
        c,d = place_poi(poi_id = i)
        for category in d:
            for item in list(newlist.keys()):
                if category == item:
                    newlist.get(item).append(c)
    return newlist

def place_poi(poi_id):

    url_place = 'https://api.sygictravelapi.com/1.1/en/places/'+str(poi_id)
    global headers
    places = requests.get(url_place,headers=headers)
    c = json.loads(places.content).get('data').get('place').get('name')
    d = json.loads(places.content).get('data').get('place').get('categories')
    return c,d