from flask_restful import Resource
import requests
from database.config import config
from datetime import date

class weatherdata(Resource):
    def post(self,city_name):
        api_key="70fe7371be9749a78e990750222706"
        base_url = "http://api.weatherapi.com/v1/current.json?"
        complete_url = base_url + "key=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        data = response.json()
        current_date = date.today()
        temp_c=data['current']['temp_c']
        temp_f=data['current']['temp_f']
        condition=data['current']['condition']['text']
        humidity = data['current']['humidity']

        conn = config()
        cur = conn.cursor()
        cur.execute('INSERT INTO weather (city_name, min_c, temp_f, weather_condition,humidity,date)'
                'VALUES (%s, %s, %s, %s)',
                (city_name,
                 temp_c,
                 temp_f,
                 condition,humidity,current_date)
                )
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

