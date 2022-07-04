from flask import Flask, render_template, session
from functions import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_KEY')

@app.route("/")
def index():
    #first time entering the page, highscore = 0
    if 'highscore' not in session:
        session['highscore'] = 0

    return render_template("index.html")

@app.route("/play")
def play():
    #id like to redirect to homepage if the user tries to play cold
    return render_template("play.html")



if __name__ == '__main__':
    app.run(debug=True)