# "postgresql://weather:shivam13@localhost:5432/weatherdb"
from ..database.db import db

class WeatherModel(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String())
    temp_c= db.Column(db.Integer())
    temp_f= db.Column(db.Integer())                                   
    weather_condition= db.Column(db.String())                                    
    humidity = db.Column(db.Integer())                                     
    date = db.Column(db.Date())                                   

    def __init__(self, city_name,temp_c,temp_f,weather_condition,humidity,date):
        self.city_name = city_name
        self.temp_c = temp_c
        self.temp_f = temp_f
        self.weather_condition = weather_condition
        self.humidity = humidity
        self.date = date

    def __repr__(self):
        return f"<weather {self.city_name}>"