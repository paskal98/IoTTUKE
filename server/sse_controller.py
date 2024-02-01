import json
import queue
import threading
import time

from flask import Flask, Response
from flask_cors import CORS

from server.mongo import process_data
from server.mqtt_client import message_queue, run_mqtt_client
from server.services import get_outside_temperature

app = Flask(__name__)
CORS(app)

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
            "identity": '1',
            "usageTime": '1h 38min',
            "lastActivity": '1min'
        },
        {
            "type": 'lamp',
            "name": 'Smart Lightning',
            "identity": '№0',
            "usageTime": '0min',
            "lastActivity": '0min'
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
                data["computers"][0]["usageElectricity"] = payload["energy"]
                data["computers"][0]["moneySpent"] = round((payload["energy"] * 0.55),2 )

                data["total"]["usageElectricity"] = data["computers"][0]["usageElectricity"]
                data["total"]["moneySpent"] = data["computers"][0]["moneySpent"]


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




if __name__ == '__main__':
    # Run MQTT client in its own thread
    mqtt_thread = threading.Thread(target=run_mqtt_client)
    mqtt_thread.start()

    # Start Flask application
    app.run(debug=True, threaded=True, port=4001)