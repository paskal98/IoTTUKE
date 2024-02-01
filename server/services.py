import requests
import slack
from attributes import *


def get_outside_temperature(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': WEATHER_API,
        'units': 'metric',
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            print(temperature)
            return temperature
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")



def shouldSendTemperatureAllert(outsideTemp, insideTemp, isWindowOpen, comfortTemp):
    if comfortTemp is None or outsideTemp is None or insideTemp is None:
        raise ValueError("One or more temperature values are missing.")

    if outsideTemp <= 0:
        raise ValueError("Outside temperature is below freezing. Alert suppressed.")

    if comfortTemp <= 0:
        raise ValueError("Comfort temperature is below freezing. Alert suppressed.")

    return isWindowOpen and insideTemp < comfortTemp and outsideTemp <= insideTemp


def send_slack_notification(msg):
    if shouldSendTemperatureAllert(get_outside_temperature(CITY), LATEST_TEMPERATURE, DOOR_CLOSED, COMFORT_TEMPERATURE):
        client = slack.WebClient(token=SLACK_BOT_API)
        client.chat_postMessage(channel="#atomic-bomb", text=msg)

def set_comfort_temperature_service(comfort_temperature):
    global COMFORT_TEMPERATURE
    COMFORT_TEMPERATURE = comfort_temperature
    print(COMFORT_TEMPERATURE)
    send_slack_notification("Clouse window")