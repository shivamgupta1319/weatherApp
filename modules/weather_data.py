from flask_restful import Resource
import requests
from database.config import config


class weatherdata(Resource):
    def post(self,city_name):
        day = "3"
        api_key="70fe7371be9749a78e990750222706"
        base_url = "http://api.weatherapi.com/v1/forecast.json?"
        complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&days=" + day
        response = requests.get(complete_url)
        x = response.json()

        # conn = config()
        # cur = conn.cursor()
        # cur.execute('INSERT INTO weather (city_name, min_temp, max_temp, weather_type,data)'
        #         'VALUES (%s, %s, %s, %s)',
        #         (cityname,
        #          temp_min,
        #          temp_max,
        #          weather_type,data)
        #         )
        # data = cur.fetchall()
        # cur.close()
        # conn.close()
        return x

