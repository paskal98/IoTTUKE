import threading
from mqtt_client import create_mqtt_client
from web_server import app

# daniil
def run_mqtt():
    
    mqtt_client = create_mqtt_client()
    mqtt_client.loop_forever()

if __name__ == '__main__':
    mqtt_thread = threading.Thread(target=run_mqtt)
    mqtt_thread.start()
    app.run(debug=True, threaded=True)
