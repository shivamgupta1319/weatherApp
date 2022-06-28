from flask_restful import Api
from flask import Flask
from .modules import weather_data,models
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='')
api = Api(app)
CORS(app, resources={r"*": {"origins": "*"}})
models.db()


api.add_resource(weather_data.weatherdata,'/data/<city_name>')


if __name__ == '__main__':
    
    app.run(debug=True)