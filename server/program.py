import threading
import concurrent.futures
from mqtt_client import create_mqtt_client
from web_server import app

def run_mqtt():
    mqtt_client = create_mqtt_client()
    mqtt_client.loop_forever()

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        mqtt_future = executor.submit(run_mqtt)
        web_server_future = executor.submit(app.run, debug=True, threaded=True)

        # Wait for both tasks to complete
        concurrent.futures.wait([mqtt_future, web_server_future], return_when=concurrent.futures.FIRST_EXCEPTION)
