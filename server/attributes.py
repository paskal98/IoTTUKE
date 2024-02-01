
MONGO_URI = "mongodb+srv://danilbond49:maker@cluster0.6h6gsaf.mongodb.net/?retryWrites=true&w=majority"
MONGO_DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"
MONGO_DATE_FORMAT = "%d/%m/%Y"

WEATHER_API = '52ebcb1d74b5509f0eb32d9d60d595a7'
SLACK_BOT_API='xoxb-6563040973363-6563214400386-BY6SwsxmpsRhfFZyQnwWI00E'
CITY = 'Kosice'
COMFORT_TEMPERATURE = 21

LATEST_TEMPERATURE = 0

DOOR_CLOSED = True
WINDOW_CLOSED = True

MORNING_TURN_ON = True
EVENING_TURN_OFF = True

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
            "identity": 1,
            "usageTime": "0min",
            "lastActivity": "0min",
            "isActive": True
        },
        {
            "type": 'lamp',
            "name": 'Smart Lightning',
            "identity": 2,
            "usageTime": '0min',
            "lastActivity": '0min',
            "isActive": True
        }
    ],

    "settings": [
        {
            "title": "Scenarios",
            "type": 'scenario',
            "options": [
                {
                    "id": 1,
                    "name": "Turn off electricity",
                    "isActive": True
                },
                {
                    "id": 2,
                    "name": "Turn on electricity",
                    "isActive": True
                },
                {
                    "id": 3,
                    "name": "Scheduled electricity",
                    "isActive": False
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