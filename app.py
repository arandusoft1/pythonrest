# -*- coding: UTF-8 -*-
#
# Install dependencies:
#
# pip install -r examples/rest_api/requirements.txt
#
# Running in development:
#
# python examples/rest_api/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
