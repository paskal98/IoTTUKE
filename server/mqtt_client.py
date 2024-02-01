import json
import paho.mqtt.client as mqtt
import queue

message_queue = queue.Queue()
temperature_queue = queue.Queue()
door_sensor_queue = queue.Queue()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #client.subscribe("gateway/zigbee/socket")
    client.subscribe("gateway/zigbee/door sensor")
    client.subscribe("gateway/zigbee/temperature_humidity")

def on_message(client, userdata, msg):
    message = {'topic': msg.topic, 'payload': msg.payload.decode()}
    payload_dict = json.loads(msg.payload)
    if "temperature" in msg.topic:
        #process_data("Temperature", payload_dict)
        temperature_queue.put(payload_dict)
        print(payload_dict)
        
    #elif "socket" in msg.topic:
        #process_data("Socket", payload_dict)
    elif "door sensor" in msg.topic:
        door_sensor_queue.put(payload_dict)
        print(payload_dict)
    print("Received topic:", msg.topic)
    message_queue.put(json.dumps(message))

def create_mqtt_client():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set('maker', 'this.is.mqtt')
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect("147.232.34.94", 1883, 60)
    return mqtt_client

def getLatestTemperature():
    last_temperature = None
    while not temperature_queue.empty():
        temperature_data = temperature_queue.get()
        if 'temperature' in temperature_data:
            last_temperature = temperature_data['temperature']
    return last_temperature

def getLatestDoorStatus():
    last_door_status = None
    while not door_sensor_queue.empty():
        door_data = door_sensor_queue.get()
        if 'contact' in door_data:
            last_door_status = door_data['contact']
    return last_door_status


