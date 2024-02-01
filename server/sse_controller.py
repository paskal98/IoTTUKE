from random import randint

from flask import Flask, Response, jsonify
import json
import time
from threading import Thread
from services import *

from flask_cors import CORS

app = Flask(__name__)

data = {
    "air": {
        "temperature": {
            "inside": 17,
            "outside": -3
        },
        "humidity": 20,
        "comfortRate": "Low"
    },
    "visitors": {
        "today": 23,
        "week": 213,
        "month": 677
    },
    "total": {
        "usageElectricity": 322,
        "moneySpent": 54.45
    },
    "computers": [
        {
            "name": 'PC1',
            "usageTime": 123.3,
            "usageLast": 5,
            "usageElectricity": 0.5,
            "moneySpent": 23.5
        }
    ],
    "switchables": [
        {
            "type": 'socket',
            "name": 'Smart Socket',
            "identity": '№12',
            "usageTime": '1h 38min',
            "lastActivity": '1min'
        },
        {
            "type": 'lamp',
            "name": 'Smart Lightning',
            "identity": '№1',
            "usageTime": '3h 38min',
            "lastActivity": '50min'
        }
    ],
    "settings": [
        {
            "title": "Scenarios",
            "type": 'scenario',
            "options": [
                {
                    "id": 1,
                    "name": "Turn off electricity"
                },
                {
                    "id": 2,
                    "name": "Turn on electricity"
                },
                {
                    "id": 3,
                    "name": "Scheduled electricity"
                }
            ]
        },
        {
            "title": "Alerts",
            "type": 'alert',
            "options": [
                {
                    "id": 1,
                    "name": "Door"
                },
                {
                    "id": 2,
                    "name": "Server"
                },
                {
                    "id": 3,
                    "name": "Weather"
                }
            ]
        }
    ]
}

def sse_stream():
    while True:

        # mqqt requets
        # db requets
        # data seting up

        json_data = json.dumps(data)
        yield f"data:{json_data}\n\n"
        time.sleep(3)
        data["air"]["humidity"] = randint(1, 100)
        data["air"]["temperature"]["inside"] = randint(18, 25)
        data["air"]["temperature"]["outside"] = randint(-10, 10)

def register_sse_routes(app):
    CORS(app)
    @app.route('/rates')
    def sse_request():
        return Response(sse_stream(), content_type='text/event-stream')

