from flask import Flask, request, jsonify, json, render_template
#from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS
#import os 

from app_models import db, video_text
from app import app

@app.route('/')
def main():

    id = 1
    video_id = 1
    segment_number = 1
    full_text = 'hello'
    starttime="00:00:00"
    endtime = "00:00:59"
    if db.session.query(video_text).filter(video_text.id == id).count() == 0:
        data = video_text(id, video_id,segment_number,full_text,starttime,endtime)
        db.session.add(data)
        db.session.commit()
    #return render_template('login.html')

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

      if db.session.query(numbers).filter(numbers.Number1 == Number1).count() == 0:
          data = numbers(Number1, Number2)
          db.session.add(data)
          db.session.commit()

      return (str(sum) + ' is the total sum of these two numbers')

if __name__ == '__main__':
   app.run(debug = True)