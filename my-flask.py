from flask import Flask
import psutil as ps

app = Flask(__name__)

memo = int(ps.virtual_memory().used / 1024 ** 3)


@app.route('/')
def index():
    hello_world = 'Hello World!'
    return f'''
    <html>
        <head>
            <title>Kroos Discord Bot</title>
        </head>
        <body>
            <h1>{hello_world}</h1>
            <h2>{memo}</h2>
        </body>
    </html>'''


# C:\Users\KAMSON-PC\PycharmProjects\python-random\set FLASK_APP=my-flask.py
# flask run
# or
# py -m flask run
# flask run --host=0.0.0.0
