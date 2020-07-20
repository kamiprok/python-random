from flask import Flask
from datetime import datetime
from random import randrange


app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    rand = randrange(1, 101)
    hello_world = 'Hello World!'
    return f'''
    <html>
        <head>
            <title>Kroos Discord Bot</title>
        </head>
        <body>
            <h1>{hello_world}</h1>
            <h2>{now}</h2>
            <h3>{rand}</h3>
        </body>
    </html>'''


app.run()

# C:\Users\KAMSON-PC\PycharmProjects\python-random\set FLASK_APP=myflask.py
# flask run
# or
# py -m flask run
# flask run --host=0.0.0.0
