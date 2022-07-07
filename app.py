from flask import Flask, render_template, session, request, flash
from functions import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_KEY')

headers = initialise_bot()
dataList = []

@app.route("/", methods=['GET', 'POST'])
def index():
    #first time entering the page, highscore = 0
    if ('highscore' not in session or session['highscore'] == 0) and request.method == 'GET':
        session['highscore'] = 0
        return render_template("index.html")
    
    #if this is a request for getting new data
    if(request.method == 'POST'):
        dataFile = "data.txt"
        print('GETTING NEW DATA')
        dataList = get_subreddits(dataFile)

        #this will be gone later DW

        #send a flash message over to the HTML so users know it be loading
        flash('Loading...', category='info')
        return render_template("index.html")


@app.route("/play", methods=['GET', 'POST'])
def play():
    #id like to redirect to homepage if the user tries to play cold
    if request.method == 'GET':
        session['score'] = 0
        return render_template("play.html")
    else: #this is when the user clicks up or downvote
        session['score'] += 1
        return render_template("play.html")




if __name__ == '__main__':
    app.run(debug=True)