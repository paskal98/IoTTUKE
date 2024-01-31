import requests
import slack

WEATHER_API = '52ebcb1d74b5509f0eb32d9d60d595a7'
SLACK_BOT_API='xoxb-6563040973363-6563214400386-BY6SwsxmpsRhfFZyQnwWI00E'

def get_outside_temperature(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Make sure to replace 'YOUR_API_KEY' with your actual API key
    params = {
        'q': city_name,
        'appid': WEATHER_API,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            return temperature
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")


def send_slack_notification(msg):
    client = slack.WebClient(token=SLACK_BOT_API)
    client.chat_postMessage(channel="#atomic-bomb", text=msg)

def monitor_temperature_condition(outsideTemp, insideTemp):
    current_temperature = 30
    if insideTemp < 20:
        send_slack_notification("Temperature is too low. Windows may be opened")