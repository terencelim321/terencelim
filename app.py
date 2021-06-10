from flask import Flask, request, jsonify, json, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
#from nltk.corpus import stopwords
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
    
    
    
    string_of_ids = ''
    if request.method == 'POST':
      string_of_ids = request.form['seg_ids']
      
    else:
      string_of_ids = request.args.get('seg_ids')

    arr_of_ids = string_of_ids.split(',')
    #string_of_ids = string_of_ids.replace(',', '')
    
    all_text = []
    for i in arr_of_ids:
        text = video_text.query.filter_by(id=float(i)).first()
        text = text.full_text
        all_text.append(text)
        
    #all_text_json = json.dumps(all_text)
    # Create stopword list:
    #stopwords= set(stopwords.words("english"))
    stopwords = ["able","about","above","abroad","according","accordingly","across","actually","adj","after","afterwards","again","against","ago","ahead","ain't","all","allow","allows","almost","alone","along","alongside","already","also","although","always","am","amid","amidst","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","a's","aside","ask","asking","associated","at","available","away","awfully","back","backward","backwards","be","became","because","become","becomes","becoming","been","before","beforehand","begin","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","came","can","cannot","cant","can't","caption","cause","causes","certain","certainly","changes","clearly","c'mon","co","co.","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","c's","currently","dare","daren't","definitely","described","despite","did","didn't","different","directly","do","does","doesn't","doing","done","don't","down","downwards","during","each","edu","eg","eight","eighty","either","else","elsewhere","end","ending","enough","entirely","especially","et","etc","even","ever","evermore","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","fairly","far","farther","few","fewer","fifth","first","five","followed","following","follows","for","forever","former","formerly","forth","forward","found","four","from","further","furthermore","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","had","hadn't","half","happens","hardly","has","hasn't","have","haven't","having","he","he'd","he'll","hello","help","hence","her","here","hereafter","hereby","herein","here's","hereupon","hers","herself","he's","hi","him","himself","his","hither","hopefully","how","howbeit","however","hundred","i'd","ie","if","ignored","i'll","i'm","immediate","in","inasmuch","inc","inc.","indeed","indicate","indicated","indicates","inner","inside","insofar","instead","into","inward","is","isn't","it","it'd","it'll","its","it's","itself","i've","just","k","keep","keeps","kept","know","known","knows","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","likewise","little","look","looking","looks","low","lower","ltd","made","mainly","make","makes","many","may","maybe","mayn't","me","mean","meantime","meanwhile","merely","might","mightn't","mine","minus","miss","more","moreover","most","mostly","mr","mrs","much","must","mustn't","my","myself","name","namely","nd","near","nearly","necessary","need","needn't","needs","neither","never","neverf","neverless","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","no-one","nor","normally","not","nothing","notwithstanding","novel","now","nowhere","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","one's","only","onto","opposite","or","other","others","otherwise","ought","oughtn't","our","ours","ourselves","out","outside","over","overall","own","particular","particularly","past","per","perhaps","placed","please","plus","possible","presumably","probably","provided","provides","que","quite","qv","rather","rd","re","really","reasonably","recent","recently","regarding","regardless","regards","relatively","respectively","right","round","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","since","six","so","some","somebody","someday","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that's","that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","there'd","therefore","therein","there'll","there're","theres","there's","thereupon","there've","these","they","they'd","they'll","they're","they've","thing","things","think","third","thirty","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","till","to","together","too","took","toward","towards","tried","tries","truly","try","trying","t's","twice","two","un","under","underneath","undoing","unfortunately","unless","unlike","unlikely","until","unto","up","upon","upwards","us","use","used","useful","uses","using","usually","v","value","various","versus","very","via","viz","vs","want","wants","was","wasn't","way","we","we'd","welcome","well","we'll","went","were","we're","weren't","we've","what","whatever","what'll","what's","what've","when","whence","whenever","where","whereafter","whereas","whereby","wherein","where's","whereupon","wherever","whether","which","whichever","while","whilst","whither","who","who'd","whoever","whole","who'll","whom","whomever","who's","whose","why","will","willing","wish","with","within","without","wonder","won't","would","wouldn't","yes","yet","you","you'd","you'll","your","you're","yours","yourself","yourselves","you've","zero","a","how's","i","when's","why's","b","c","d","e","f","g","h","j","l","m","n","o","p","q","r","s","t","u","uucp","w","x","y","z","I","www","amount","bill","bottom","call","computer","con","couldnt","cry","de","describe","detail","due","eleven","empty","fifteen","fifty","fill","find","fire","forty","front","full","give","hasnt","herse","himse","interest","itse”","mill","move","myse”","part","put","show","side","sincere","sixty","system","ten","thick","thin","top","twelve","twenty","abst","accordance","act","added","adopted","affected","affecting","affects","ah","announce","anymore","apparently","approximately","aren","arent","arise","auth","beginning","beginnings","begins","biol","briefly","ca","date","ed","effect","et-al","ff","fix","gave","giving","heres","hes","hid","home","id","im","immediately","importance","important","index","information","invention","itd","keys","kg","km","largely","lets","line","'ll","means","mg","million","ml","mug","na","nay","necessarily","nos","noted","obtain","obtained","omitted","ord","owing","page","pages","poorly","possibly","potentially","pp","predominantly","present","previously","primarily","promptly","proud","quickly","ran","readily","ref","refs","related","research","resulted","resulting","results","run","sec","section","shed","shes","showed","shown","showns","shows","significant","significantly","similar","similarly","slightly","somethan","specifically","state","states","stop","strongly","substantially","successfully","sufficiently","suggest","thered","thereof","therere","thereto","theyd","theyre","thou","thoughh","thousand","throug","til","tip","ts","ups","usefully","usefulness","'ve","vol","vols","wed","whats","wheres","whim","whod","whos","widely","words","world","youd","youre"]
    #sets all stop words
    #stopwords.add('(')
    #stopwords.add(')')
    #stopwords.add('[')
    #stopwords.add(']')
    #stopwords.add("``")
    #stopwords.add("''")
    #stopwords.add(",")
    #stopwords.add("'s")
    #stopwords.add("'")
    #stopwords.add('""')
    #stopwords.add("n't")
    #stopwords.add("'re")
    
    stopwords.append('(')
    stopwords.append(')')
    stopwords.append('[')
    stopwords.append(']')
    stopwords.append("``")
    stopwords.append("''")
    stopwords.append(",")
    stopwords.append("'s")
    stopwords.append("'")
    stopwords.append('""')
    stopwords.append("n't")
    stopwords.append("'re")
    stopwords.append("'can")
    stopwords.append("'you")
    stopwords.append("nav")
    stopwords.append("'m")
    stopwords.append("'do")
    #return str(stopwords)
    tokenized_word = word_tokenize(str(all_text))
    #print(tokenized_word)
    
    #checks the text and filters out all the stop words inside
    filtered_sent=[]
    for w in tokenized_word:
        if w not in stopwords:
            filtered_sent.append(w)

    
    fdist = FreqDist(filtered_sent)
    #top10
    top_10 = fdist.most_common(10)


    freq_json = jsonify(top_10)
    #return  freq_json
    
    return freq_json




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


