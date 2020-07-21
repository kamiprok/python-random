from flask import Flask, render_template
from datetime import datetime
from random import randrange
from pymongo import MongoClient


app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    rand = randrange(1, 101)
    hello_world = 'Hello World!'
    return render_template('index.html', now=now, rand=rand, say=hello_world)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/data')
def data():
    client = MongoClient('MongoDBConnectionString')
    db = client.MongoDB
    collection = db.collection
    list = []
    for i in collection.find({}):
        list.append(i)
    return render_template('data.html', len=len(list), list=list)


app.run(host='0.0.0.0', port=8080)

# C:\Users\KAMSON-PC\PycharmProjects\python-random\set FLASK_APP=myflask.py
# flask run
# or
# py -m flask run
# flask run --host=0.0.0.0
# with app.run() you can run flask app my py myflask.py instead of setting variable and running flask run
# data needs connection string to db and pulls data from db
