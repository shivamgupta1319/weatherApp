from flask_restful import Api
from database.config import config
from flask import Flask, jsonify, render_template, request, send_from_directory
from modules import weather_data,models

app = Flask(__name__, static_url_path='', static_folder='')
api = Api(app)




@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')


api.add_resource(weather_data.weatherdata,'/data/<city_name>')


if __name__ == '__main__':
    models.db()
    app.run(debug=True)