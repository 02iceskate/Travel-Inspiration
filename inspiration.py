import requests
import numpy as np
import pandas as pd
import json
from requests_futures.sessions import FuturesSession
from titlecase import titlecase
from location import location_id


with open('./data_city.json', 'r') as myfile:  #the json file contains all the cities which the api developer is working on 
    data=myfile.read()

obj = json.loads(data)

cities = []
cities = [obj[i].get('name').rstrip().lower() for i in range(0,len(obj))]

popularity_index = []
nightlife_indices =[]
countries = []

session = FuturesSession(max_workers=16)

# Create a dataframe to store all the indinces and saved it as csv file
#for city in cities[0:10]:
    #country, popularity, nightlife_index = location_id(session,city)
    #popularity_index.append(popularity)
    #nightlife_indices.append(nightlife_index )
    #countries.append(country)

#df = pd.DataFrame(np.column_stack([countries,cities[0:10],popularity_index, nightlife_indices]), columns = ['Country', 'City','Popularity_index','Nightlife_index'])
#df['Average'] = (df['Popularity_index'].astype('float') + df['Nightlife_index'].astype('float'))/2
#df.to_csv(r'C:\\Users\\user\\Documents\\Tech_challenge\\city_index.csv',index = None, header=True)

df_csv = pd.read_csv('..\\Tech Challenge\\city_index.csv') #the csv file only  saves the first 250 cities as there is
    #limitation of request per day

# Ask the client to fill in
popular_marks = float(input("Please input the popularity you prefer: (5 is the highest)"))
nightlife_marks = float(input("Please input the nightlife index you prefer: (5 is the highest)"))


# we will weight the one higher with the higher marks
if popular_marks > nightlife_marks: 
    calculation = popular_marks*0.7 + nightlife_marks*0.3
elif popular_marks == nightlife_marks:
    calculation = popular_marks*0.5 + nightlife_marks*0.5
else:
    calculation = popular_marks*0.3 + nightlife_marks*0.7

df_csv['Difference'] = abs(df_csv['Average'] - calculation)

# Return the first three suggestions
first_suggestion_country = df_csv.nsmallest(10,'Difference')[df_csv.nsmallest(10,'Difference')['Popularity_index'] > 3.5].values.tolist()[0][0]
first_suggestion_city = df_csv.nsmallest(10,'Difference')[df_csv.nsmallest(10,'Difference')['Popularity_index'] > 3.5].values.tolist()[0][1]
second_suggestion_country = df_csv.nsmallest(10,'Difference')[df_csv.nsmallest(10,'Difference')['Popularity_index'] > 3.5].values.tolist()[1][0]
second_suggestion_city = df_csv.nsmallest(10,'Difference')[df_csv.nsmallest(10,'Difference')['Popularity_index'] > 3.5].values.tolist()[1][1]
third_suggestion_country = df_csv.nsmallest(10,'Difference')[df_csv.nsmallest(10,'Difference')['Popularity_index'] > 3.5].values.tolist()[2][0]
third_suggestion_city = df_csv.nsmallest(10,'Difference')[df_csv.nsmallest(10,'Difference')['Popularity_index'] > 3.5].values.tolist()[2][1]

print("\n1st suggested location: "+"\nCountry: "+first_suggestion_country+"\nCity: "+titlecase(first_suggestion_city))
print("\n2nd suggested location: "+"\nCountry: "+second_suggestion_country+"\nCity: "+titlecase(second_suggestion_city))
print("\n3rd suggested location: "+"\nCountry: "+third_suggestion_country+"\nCity: "+titlecase(third_suggestion_city))

