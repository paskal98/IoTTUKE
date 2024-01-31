import json
from services import *
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://danilbond49:maker@cluster0.6h6gsaf.mongodb.net/?retryWrites=true&w=majority"

MONGO_DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
database = client.get_database("MQTTDB")


print("Storing")
def process_data(collectionName, payload):
    collection = database.get_collection(collectionName)
    now = datetime.now()
    try:
        if collectionName == "Temperature":
            insideTemp = payload.get('temperature')
            outsideTemp = get_outside_temperature("Kosice")
            if outsideTemp is None:
                outsideTemp = 0
            print("Outside TEMP ", outsideTemp)
            monitor_temperature_condition(outsideTemp, insideTemp)
            document = {
                "outside": outsideTemp,
                "inside": insideTemp,
                "timestamp": int(now.timestamp()),
                "datetime": now.strftime(MONGO_DATETIME_FORMAT),
            }
        elif collectionName == "Socket":
            document = {
                "outside": -3,
                "inside": 13,
                "timestamp": int(now.timestamp()),
                "datetime": now.strftime(MONGO_DATETIME_FORMAT),
            }
        result = collection.insert_one(document)
        print("Saved in Mongo document ID", result.inserted_id)
    except Exception as ex:
        print(ex)
