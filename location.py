import requests
import json
import os

#retrieve info from Zomato
user_key = os.environ.get('USER-KEY')

headers = {"Accept": "application/json",
          "user-key": user_key}

def location_id(session, city):  #return the location id of a city
    
    url = 'https://developers.zomato.com/api/v2.1/locations?query='+city
    data = {"query": city, "count":1}
    global headers
    res_city = requests.post(url,data=data,headers=headers)
    x = json.loads(res_city.text)
    y = x.get('location_suggestions')[0].get('entity_id') #retreive the location id
    z = x.get('location_suggestions')[0].get('entity_type') # retrieve 'city' or 'country'
    a = x.get('location_suggestions')[0].get('country_name') #retrieve corresponding country name
    
    def location_details(entity_id,entity_type):
        url = 'https://developers.zomato.com/api/v2.1/location_details?entity_id='+str(entity_id)+'&entity_type='+entity_type
        data_loc = {"entity_id": entity_id, "entity_type": entity_type}
        res_loc = requests.post(url,data=data_loc,headers=headers)
        popularity = json.loads(res_loc.text).get('popularity')  #return the popularity index of a city
        nightlife_index = json.loads(res_loc.text).get('nightlife_index') ##return the nightlife index of a city
        
        return(popularity,nightlife_index)
    
    b,c = location_details(y,z)
    return (a,b,c)

