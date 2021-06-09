from flask import Flask, request, jsonify, json, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
#dev database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/postdata'
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("dbURL")
#production database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

class video_text(db.Model):
    __tablename__ = 'video_text'

    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, nullable=False)
    segment_number = db.Column(db.Integer, nullable=False)
    full_text = db.Column(db.String(2000), nullable=False)
    starttime = db.Column(db.Time , nullable=False)
    endtime = db.Column(db.Time , nullable=False)

    def __init__(self, id, video_id, segment_number, full_text, starttime, endtime):
        self.id = id
        self.video_id= video_id
        self.segment_number = segment_number
        self.full_text = full_text
        self.starttime = starttime
        self.endtime = endtime

    
@app.route('/',methods = ['POST', 'GET'])
def main():
    arr_of_ids = []
    if request.method == 'POST':
      arr_of_ids = request.form['seg_ids']
      
    else:
      arr_of_ids = request.args.get('seg_ids')
      

    text_1 = video_text.query.filter_by(id=1).first()
    text_2 = video_text.query.filter_by(id=2).first()
    

    return text_1
    #return render_template('login.html')
    #https://sumtestterence.herokuapp.com/?seg_ids=1,2
    

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


