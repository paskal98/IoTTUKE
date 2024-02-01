import json
import paho.mqtt.client as mqtt
import queue
from mongo import process_data
from attributes import *
from mongo import get_socket_week_from_db
from datetime import datetime, time
from services import send_slack_notification


import paho.mqtt.publish as publish

MQTT_HOST = "147.232.34.94"
MQTT_PORT = 1883
MQTT_USERNAME = 'maker'
MQTT_PASSWORD = 'this.is.mqtt'

def mqtt_publish(topic, payload):
    auth = {'username': MQTT_USERNAME, 'password': MQTT_PASSWORD}
    publish.single(topic, payload=json.dumps(payload), hostname=MQTT_HOST, port=MQTT_PORT, auth=auth)

def is_more_than_6pm():
    current_time = datetime.now().time()
    six_pm = time(18, 0)
    return current_time > six_pm

def is_between_6am_and_6pm():
    current_time = datetime.now().time()
    six_am = time(6, 0)
    six_pm = time(18, 0)
    return six_am <= current_time <= six_pm

# This queue will hold MQTT messages for SSE to consume
message_queue = queue.Queue()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("gateway/zigbee/socket")
    client.subscribe("gateway/zigbee/door sensor")
    client.subscribe("gateway/zigbee/temperature_humidity")

def on_message(client, userdata, msg):
    # print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    # Here, simply enqueue the message for the SSE endpoint to consume
    message_queue.put((msg.topic, msg.payload.decode()))
    payload_dict = json.loads(msg.payload)
    if "temperature" in msg.topic:
        send_slack_notification("Close window. Temperature is too low")
        process_data("Temperature", payload_dict)
    elif "socket" in msg.topic:
        process_data("Socket", payload_dict)
    elif "door" in msg.topic:
        global DOOR_CLOSED
        print(EVENING_TURN_OFF)
        if payload_dict.get('contact') == True:
            DOOR_CLOSED = True
            if is_more_than_6pm() and EVENING_TURN_OFF:
                print(EVENING_TURN_OFF)
                payload = {"state_l1": "OFF", "state_l2": "OFF"}
                data["switchables"][0]["isActive"] = False
                data["switchables"][1]["isActive"] = False
                mqtt_publish("gateway/zigbee/socket/set", payload)
        elif payload_dict.get('contact') == False:
            DOOR_CLOSED = False
            if is_between_6am_and_6pm() and MORNING_TURN_ON:
                print("asdasd")
                payload = {"state_l1": "ON", "state_l2": "ON"}
                data["switchables"][0]["isActive"] = True
                data["switchables"][1]["isActive"] = True
                mqtt_publish("gateway/zigbee/socket/set", payload)
    elif "window" in msg.topic:
        global WINDOW_CLOSED
        if payload_dict.get('contact') == True:
            WINDOW_CLOSED = True
        else:
            WINDOW_CLOSED = False


def create_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # Assuming MQTT broker requires authentication
    client.username_pw_set('maker', 'this.is.mqtt')
    client.connect("147.232.34.94", 1883, 60)
    return client

# Function to run MQTT client in its own thread
def run_mqtt_client():
    client = create_mqtt_client()
    client.loop_start()  # Starts network loop in a separate thread