import json
import queue
import threading
import time

from flask import Flask, Response, request, jsonify
from flask_cors import CORS

from mongo import process_data, get_socket_week_from_db
from mqtt_client import message_queue, run_mqtt_client
from services import get_outside_temperature
from temperature_controller import register_temperature_routes

import paho.mqtt.publish as publish

MQTT_HOST = "147.232.34.94"
MQTT_PORT = 1883
MQTT_USERNAME = 'maker'
MQTT_PASSWORD = 'this.is.mqtt'

app = Flask(__name__)
CORS(app)
register_temperature_routes(app)

start_time = time.time()

data = {
    "air": {
        "temperature": {
            "inside": None,
            "outside": None
        },
        "humidity": None,
        "comfortRate": "Low"
    },
    "visitors": {
        "today": 23,
        "week": 213,
        "month": 677
    },
    "total": {
        "usageElectricity": 0.0,
        "moneySpent": 0.0
    },
    "computers": [
        {
            "name": 'PC1',
            "usageTime": 3.4,
            "usageLast": 0,
            "usageElectricity": None,
            "moneySpent": None
        }
    ],
    "switchables": [
        {
            "type": 'socket',
            "name": 'Smart Socket',
            "identity": 1,
            "usageTime": "0min",
            "lastActivity": "0min",
            "isActive": True
        },
        {
            "type": 'lamp',
            "name": 'Smart Lightning',
            "identity": 2,
            "usageTime": '0min',
            "lastActivity": '0min',
            "isActive": True
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

def get_working_time():
    elapsed_time = time.time() - start_time
    elapsed_hours = elapsed_time / 3600.0
    return round(elapsed_hours, 2)

def mqtt_publish(topic, payload):
    auth = {'username': MQTT_USERNAME, 'password': MQTT_PASSWORD}
    publish.single(topic, payload=json.dumps(payload), hostname=MQTT_HOST, port=MQTT_PORT, auth=auth)


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
                data["computers"][0]["usageElectricity"] = payload["energy"]
                data["computers"][0]["moneySpent"] = round((payload["energy"] * 0.55), 2)

                data["total"]["usageElectricity"] = data["computers"][0]["usageElectricity"]
                data["total"]["moneySpent"] = data["computers"][0]["moneySpent"]

                data["computers"][0]["usageTime"] = get_working_time()



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


@app.route('/switch', methods=['GET'])
def switch():
    identity = 1
    if identity:
        for device in data["switchables"]:
            if device["identity"] == identity:

                if device["isActive"]:
                    state = "OFF"
                    device["isActive"] = False
                else:
                    state = "ON"
                    device["isActive"] = True

                device["lastActivity"] = "0"
                payload = {"state_l1": state, "state_l2": state}
                mqtt_publish("gateway/zigbee/socket/set", payload)

                return jsonify({"message": "Device state updated and published to MQTT"}), 200
    else:
        return jsonify({"message": "Device state not updated"}), 200




if __name__ == '__main__':
    # Run MQTT client in its own thread
    mqtt_thread = threading.Thread(target=run_mqtt_client)
    mqtt_thread.start()

    # Start Flask application
    app.run(debug=True, threaded=True, port=4001)
