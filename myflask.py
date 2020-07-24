from flask import Flask, render_template, request, redirect
from datetime import datetime
from random import randrange
from pymongo import MongoClient

MongoDBConnectionString = 'MongoDBConnectionString'
client = MongoClient(MongoDBConnectionString, serverSelectionTimeoutMS=5000)
db = client.MongoDB
people = db.people
collection = db.collection

app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    rand = randrange(1, 101)
    hello_world = 'Hello World!'
    return render_template('index.html', now=now, rand=rand, say=hello_world)


@app.route('/data', methods=['GET'])
def data():
    return render_template('data.html', people=people)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['input']
    if name == '':
        print('empty string')
        return redirect('/data')
    else:
        name = {"name": name}
        people.insert_one(name)
        return redirect('/data')


@app.route('/clear', methods=['POST'])
def clear():
    for document in people.find():
        people.delete_one(document)
    return redirect('/data')


@app.route('/collection')
def col():
    list = []
    for i in collection.find({}):
        list.append(i)
    # doc = 'Document:'
    # for i in collection.find({}):
    #     doc = f'{doc} {i}\n'
    # print(doc)
    return render_template('collection.html', len=len(list), list=list)


app.run(debug=True, host='0.0.0.0', port=8080)

# C:\Users\KAMSON-PC\PycharmProjects\python-random\set FLASK_APP=myflask.py
# flask run
# or
# py -m flask run
# flask run --host=0.0.0.0
# with app.run() you can run flask app my py myflask.py instead of setting variable and running flask run
# data needs connection string to db and pulls data from db
