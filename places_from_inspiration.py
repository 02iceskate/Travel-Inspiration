import requests
import numpy as np
import json
from places_f import location_id, places

#retreive info from Sygic travel site

cities = ['london','osaka']  #suppose the cities generated from location.py are london and osaka
cities_id = []
countries_id = []



for city in cities:
    city_id, country_id = location_id(city)  # firstly we find out the id for the corresponding cities
    suggestion = places(place_id = city_id)
    print(city.upper())
    print('The followings are recommended:')
    print(suggestion)









