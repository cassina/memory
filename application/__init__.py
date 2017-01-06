#!/usr/bin/python

from flask import Flask, jsonify
# Config
#
#
SMOKE_URL = '/_t/smoke'

# Create app
#
#
app = Flask(__name__)


# Blueprint
#
#
@app.route(SMOKE_URL, methods=['GET'])
def smoke():
    smoke_dict = {
        'foo': 'bar'
    }
    return jsonify(smoke_dict)
