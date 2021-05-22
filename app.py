from flask import Flask, render_template, request

#declare app
app = Flask(__name__)

#start app route which is /
@app.route("/")
#declare function
def main():
    	    return render_template('app.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)