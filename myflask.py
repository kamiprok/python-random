from flask import Flask, render_template
from datetime import datetime
from random import randrange


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


app.run(host='0.0.0.0', port=8080)

# C:\Users\KAMSON-PC\PycharmProjects\python-random\set FLASK_APP=myflask.py
# flask run
# or
# py -m flask run
# flask run --host=0.0.0.0
# with app.run() you can run flask app my py myflask.py instead of setting variable and running flask run
