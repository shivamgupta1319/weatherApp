from flask_restful import Api
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .server.modules import weather_data
from .server.database import db

# db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://weather:shivam13@localhost:5432/weatherdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.db.init_app(app)
migrate = Migrate(app, db.db)
api = Api(app)
CORS(app, resources={r"*": {"origins": "*"}})


api.add_resource(weather_data.weatherdata,'/data/<city_name>')


if __name__ == '__main__':
    
    app.run(debug=True)