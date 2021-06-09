from flask import Flask, request, jsonify, json, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

from os import path
from PIL import Image


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import mysql.connector
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import json



app = Flask(__name__)
#dev database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/bigdatavideo'
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

    return ('hello')
    #from nltk.corpus import stopwords
    #string_of_ids = ''
    #if request.method == 'POST':
      #string_of_ids = request.form['seg_ids']
      
    #else:
      #string_of_ids = request.args.get('seg_ids')

    #string_of_ids = string_of_ids.replace(',', '')
    
    #all_text = ''
    #for i in string_of_ids:
        #text = video_text.query.filter_by(id=float(i)).first()
        #text = text.full_text
        #all_text += ' ' + text


    #stopwords = set(stopwords.words('english'))
    # Create stopword list:
    #sets all stop words
    #stopwords.add('(')
    #stopwords.add(')')
    #stopwords.add('[')
    #stopwords.add(']')
    #stopwords.add("``")
    #stopwords.add("''")
    #stopwords.add(",")
    #stopwords.add("s")
    #stopwords.add("'")

    #tokenized_word = word_tokenize(all_text)
    #print(tokenized_word)

    #checks the text and filters out all the stop words inside
    #filtered_sent=[]
    #for w in tokenized_word:
        #if w not in stopwords:
            #filtered_sent.append(w)
                
    #fdist = FreqDist(filtered_sent)
    #top10
    #print(fdist.most_common(10))
    # Generate a word cloud image
    #wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)


    # Create and generate a word cloud image:
    #wordcloud = WordCloud().generate(text)

    # lower max_font_size, change the maximum number of word and lighten the background:
    #wordcloud = WordCloud(max_font_size=50, max_words=10, background_color="white").generate(text)
    #plt.figure()
    #This is to make the displayed image appear more smoothly.
    #plt.imshow(wordcloud, interpolation="bilinear")
    #plt.axis("off")
    #plt.show()
    #return filtered_sent
    #return arr_of_ids
    #return render_template('login.html')
    #https://sumtestterence.herokuapp.com/?seg_ids=1,2
    #http://127.0.0.1:5000/?seg_ids=1,2
    

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


