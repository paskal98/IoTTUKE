import json
import paho.mqtt.client as mqtt
import queue

from server.mongo import process_data

# This queue will hold MQTT messages for SSE to consume
message_queue = queue.Queue()

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code " + str(rc))
    client.subscribe("gateway/zigbee/socket")
    client.subscribe("gateway/zigbee/door sensor")
    client.subscribe("gateway/zigbee/temperature_humidity")

def on_message(client, userdata, msg):
    # print(f"Received message on {msg.topic}: {msg.payload.decode()}")
    # Here, simply enqueue the message for the SSE endpoint to consume
    message_queue.put((msg.topic, msg.payload.decode()))
    payload_dict = json.loads(msg.payload)
    if "temperature" in msg.topic:
        process_data("Temperature", payload_dict)
    elif "socket" in msg.topic:
        process_data("Socket", payload_dict)


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
