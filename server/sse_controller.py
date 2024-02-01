import json
import queue
import threading
import time

from flask import Flask, Response
from flask_cors import CORS

from mongo import process_data, get_socket_week_from_db
from mqtt_client import message_queue, run_mqtt_client
from services import get_outside_temperature

app = Flask(__name__)
CORS(app)

data = {
    "air": {
        "temperature": {
            "inside": 17,
            "outside": None
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
        try:
            topic, payloadRaw = message_queue.get()
            payload = json.loads(payloadRaw)  # Deserialize payload if it's a JSON string

            data["air"]["temperature"]["outside"] = get_outside_temperature('Kosice')
            if topic == "gateway/zigbee/temperature_humidity":
                data["air"]["temperature"]["inside"] = payload["temperature"]
                data["air"]["humidity"] = payload["humidity"]
            if topic == "gateway/zigbee/socket":
                data["total"]["usageElectricity"] = payload["energy"]
                data["total"]["usageElectricity"] = payload["energy"]

            print(f"Data updated from topic: {topic}")  # Debugging

        except queue.Empty:
            print("No new messages from MQTT.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        json_data = json.dumps(data)
        yield f"data:{json_data}\n\n"
        time.sleep(3)


@app.route('/rates')
def stream():
    return Response(sse_stream(), content_type='text/event-stream')

@app.route('/socket-info')
def stream2():
    return get_socket_week_from_db()

if __name__ == '__main__':
    # Run MQTT client in its own thread
    mqtt_thread = threading.Thread(target=run_mqtt_client)
    mqtt_thread.start()

    # Start Flask application
    app.run(debug=True, threaded=True, port=4001)