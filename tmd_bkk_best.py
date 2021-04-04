import json
import requests
import pandas as pd
import datetime as dt

token= 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjUzNjM2OTkwYmUyMTczMjhmZGM1NzljY2I0ZTIyMzEwZTdhOTdlMjFmYmE1NjA3Y2RiY2VjYjk5M2QzYjM3ZWU0MjljNzIyMmI1MTcyZDc5In0.eyJhdWQiOiIyIiwianRpIjoiNTM2MzY5OTBiZTIxNzMyOGZkYzU3OWNjYjRlMjIzMTBlN2E5N2UyMWZiYTU2MDdjZGJjZWNiOTkzZDNiMzdlZTQyOWM3MjIyYjUxNzJkNzkiLCJpYXQiOjE2MTc1MjM0NTYsIm5iZiI6MTYxNzUyMzQ1NiwiZXhwIjoxNjQ5MDU5NDU2LCJzdWIiOiIxMzc0Iiwic2NvcGVzIjpbXX0.N2_5A9K5YmpiXHMm-I-OGOnhz_tQnQ9_zluLibhHZXrjkedZ_cDY_60uagJwFtf-TcHDUkmrAvn49b-u37mjL7jy6GSi3l2bpy5HNS3pRqafftr8Ut2X8ZRIRoEKYMBN_jHHeQ0F7MRgYaHSWZrbt9Vvb_kE1EMsgFAtoWaO9WyvC-87Q1A_z93mWdUuH4vmFaGQBwhRVi9DTasW-S9WIZqza_gJ0Mdv_RrYmakOkJA4jD3fqKkFagnoMmiRBiiFAAVrTW5Zx1TeChlpDTTMeAVUDtTGMBkuyXTNlzXXTQCi5X-GJqfhlOWI4c2AiUcTuGj8RqPxvKbNkvppsryH7OieJaeFya3LmCLTabISH5zNhnrkwmoWgoPd8RqMerv5R4pOf4K-YnBc1ZJZwNNq0Snzl0EKXLp9J0Hiiyz04gT1MzAcu8hSU29Op3ozbh96tGeefKGE4qBCwGDT91NtrSODdBntar3mqHYQyWvtAruGAl6suy8tvrtxLVxyBUq2OWj9rd-i-IN5jVYs2WtAWfu82vl6RQfbq_YbgUyp9o5U4LK5MmNoZxgKIFigycbBrXoR5_qKlRb7uiG31OR5lLVvAdhzNkXrxxsOvjyiwCmIqPyBmBcOkMKpGNKGr0aJR74g5gQwdMFcDY5-d7lLNJzMidkdxe0w6hXyQSo9haU'

# Province
lat =  19.907
long = 99.832

t = dt.datetime.now()+dt.timedelta(hours=1)

url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/at"

querystring = {
    "lat":"%s"%lat,
    "lon":"%s"%long,
    "fields":"tc,rh,rain",
    "date":"%s-%02d-%02d"%(t.year,t.month,t.day),
    "hour":"%s"%(t.hour),
    "duration":"1"
   }
headers = {
   'accept': "application/json",
   'authorization': "Bearer "+token,
    }

response = requests.request("GET", url, headers=headers, params=querystring)
d=json.loads(response.text)
d =  {
        'lat': d['WeatherForecasts'][0]['location']['lat'],
        'lon': d['WeatherForecasts'][0]['location']['lon'],
        'time': d['WeatherForecasts'][0]['forecasts'][0]['time'],
        'rh': d['WeatherForecasts'][0]['forecasts'][0]['data']['rh'],
        'tc': d['WeatherForecasts'][0]['forecasts'][0]['data']['tc'],
        'rain': d['WeatherForecasts'][0]['forecasts'][0]['data']['rain']
    }
df_out = pd.read_csv('/Users/chayaponechainate/Desktop/Chayapone_TMD_Contab/TMD_data_Jay.csv')
df_out.loc[len(df_out)]=['Chiang_Rai',d['time'],d['tc'],d['rh'],d['rain']]
df_out.to_csv('/Users/chayaponechainate/Desktop/Chayapone_TMD_Contab/TMD_data_Jay.csv')
