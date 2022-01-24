import requests
import os
from dotenv import load_dotenv
import json

#class para hacer las peticiones a la api
class Weather():
    #constructor
    def __init__(self,api_key, city ):
        self.api_key = api_key
        self.city = city
    

    #metodo para obtener el clima
    def get_weather(self):
        url = 'https://weatherapi-com.p.rapidapi.com/current.json'
        querystring = {"q":self.city}
        headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': self.api_key}
        data = requests.request("GET", url, headers=headers, params=querystring)
        #gurdamos en un json
        with open ('weather.json', 'w') as f:
            json.dump(data.json(), f)
        #retornamos el json y obtenemos el clima
        with open ('weather.json', 'r') as f:
            data = json.load(f)
            forecast =[]
            city = data['location']['name']
            country = data['location']['country']
            temp = data['current']['temp_c']
            weather = data['current']['condition']['text']
            icon = data['current']['condition']['icon']
            localtime = data['location']['localtime']
            forecast.append(city)
            forecast.append(country)
            forecast.append(temp)
            forecast.append(weather)
            forecast.append(icon)
            forecast.append(localtime)
            
        return forecast

load_dotenv()

apiKey = os.getenv("API_KEY")
myweather = Weather(apiKey, 'Caracas')
print(myweather.get_weather())

