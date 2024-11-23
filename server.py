from flask import Flask, request, jsonify, Response
from random import shuffle
import sys

app = Flask(__name__)

articles = []

@app.route("/")
def home():
    return Response(open(sys.argv[1]).read(), mimetype="text/html")

@app.route('/submit', methods=['POST'])
def submit():
    global argicles
    s = request.form["article"]
    articles.append(s)
    return f"submit {s} OK"

@app.route('/random', methods=['GET'])
def get():
    global argicles
    if len(articles) == 0:
        article = "no articles submitted"
    else:
        shuffle(articles)
        article = articles[0]
    return article

@app.route('/all', methods=['GET'])
def all():
    global argicles
    if len(articles) != 0:
        shuffle(articles)
    return f"{articles}"

@app.route('/reset')
def rest():
    global articles
    articles = []
    return "rest OK"


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True ,port=2442)
