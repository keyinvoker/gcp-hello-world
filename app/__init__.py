from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import DB_USER, DB_PASS, CLOUD_SQL_PUBLIC_IP_ADDRESS, DB_NAME

app = Flask('NONSENSE')
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SESSION_COOKIE_SECURE'] = False

dbconnect_string = f'postgresql+pg8000://{DB_USER}:{DB_PASS}@{CLOUD_SQL_PUBLIC_IP_ADDRESS}/{DB_NAME}'
engine = create_engine(dbconnect_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

ma = Marshmallow(app)

CORS(app)

from app import routes