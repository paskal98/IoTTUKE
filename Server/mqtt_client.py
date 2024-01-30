import json
import paho.mqtt.client as mqtt
import queue

message_queue = queue.Queue()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("gateway/zigbee/socket")
    client.subscribe("gateway/zigbee/window")
    client.subscribe("gateway/zigbee/temperature_humidity")

def on_message(client, userdata, msg):
    message = {'topic': msg.topic, 'payload': msg.payload.decode()}
    message_queue.put(json.dumps(message))

def create_mqtt_client():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set('maker', 'this.is.mqtt')
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect("10.0.0.1", 8080, 60)
    return mqtt_client
