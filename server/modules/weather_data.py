from flask_restful import Resource
import requests
# from server.database.config import con
from datetime import date
from .Orm_model import WeatherModel
from ..database import db

class weatherdata(Resource):
    def post(self,city_name):
        api_key="70fe7371be9749a78e990750222706"
        base_url = "http://api.weatherapi.com/v1/current.json?"
        complete_url = base_url + "key=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        data = response.json()
        city_name = str(city_name)
        current_date = date.today()
        temp_c=int(data['current']['temp_c'])
        temp_f=int(data['current']['temp_f'])
        condition=str(data['current']['condition']['text'])
        humidity = int(data['current']['humidity'])
        new_data = WeatherModel(city_name=city_name, temp_c=temp_c, temp_f=temp_f, weather_condition=condition, humidity=humidity, date=current_date)
        db.db.session.add(new_data)
        db.db.session.commit()

        # conn = con()
        # cur = conn.cursor()
        # try:
        #     cur.execute('INSERT INTO weather (city_name, temp_c, temp_f, weather_condition,humidity,date)'
        #             'VALUES (%s, %s, %s, %s, %s, %s)',
        #             (city_name,
        #             temp_c,
        #             temp_f,
        #             condition,humidity,current_date)
        #             )
        # except:
        #     print("data not post")
        # data = cur.fetchall()
        # conn.commit()
        # cur.close()
        # conn.close()
        return data

