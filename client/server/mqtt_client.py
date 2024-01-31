import json
import paho.mqtt.client as mqtt
import queue
from mongo import process_data

message_queue = queue.Queue()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #client.subscribe("gateway/zigbee/socket")
    client.subscribe("gateway/zigbee/door sensor")
    client.subscribe("gateway/zigbee/temperature_humidity")

def on_message(client, userdata, msg):
    message = {'topic': msg.topic, 'payload': msg.payload.decode()}
    payload_dict = json.loads(msg.payload)
    if "temperature" in msg.topic:
        process_data("Temperature", payload_dict)
    elif "socket" in msg.topic:
        process_data("Socket", payload_dict)
    print("Received topic:", msg.topic)
    message_queue.put(json.dumps(message))

def create_mqtt_client():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set('maker', 'this.is.mqtt')
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect("147.232.34.94", 1883, 60)
    return mqtt_client
