from flask import Flask, request, jsonify, json, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS
from os import environ

app = Flask(__name__)
#dev database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/postdata'
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("dbURL")
#production database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bwtdvlbfpruyuc:a291b9482d49f67d638b5188f1934104dee5722cdc5facf539243ca05033a675@ec2-34-202-54-225.compute-1.amazonaws.com:5432/d4a674qjb8ea29'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#CORS(app)

db = SQLAlchemy(app)

class Sum(db.Model):
    __tablename__ = 'Numbers'

    Number1 = db.Column(db.Integer, primary_key=True)
    Number2 = db.Column(db.Integer, primary_key=True)
    #LastName = db.Column(db.String(2000), nullable=False)
    #AbandonEmail = db.Column(db.String(2000), nullable=False)
    #TeleID = db.Column(db.String(2000), nullable=False)

    def __init__(self, Number1, Number2):
        self.Number1 = Number1
        self.Number2 = Number2

@app.route('/')
def main():
    return render_template('login.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      num1 = request.form['num1']
      num2 = request.form['num2']

      sum = int(num1) + int(num2)
      return str(sum)
   else:
      Number1 = request.args.get('num1')
      Number2 = request.args.get('num2')
      sum = int(Number1) + int(Number2)

      if db.session.query(Sum).filter(Sum.Number1 == Number1).count() == 0:
          data = Sum(Number1, Number2)
          db.session.add(data)
          db.session.commit()

      return (str(sum) + ' is the total sum of these two numbers')

if __name__ == '__main__':
   app.run(debug = True)