
#production database
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#CORS(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__, instance_relative_config=True)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/postdata'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")

db = SQLAlchemy(app)

    
