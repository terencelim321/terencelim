from flask import Flask, request, jsonify, json, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os



app = Flask(__name__)
#dev database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/bigdatavideo'
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("dbURL")
#production database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)



