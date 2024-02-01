from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from server.services import get_outside_temperature, monitor_temperature_condition
from attributes import *

# Set the Stable API version when creating a new client
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
database = client.get_database("MQTTDB")

def process_data(collectionName, payload):
    now = datetime.now()
    try:
        if collectionName == "Temperature":
            insideTemp = payload.get('temperature')
            humidity = payload.get('humidity')
            outsideTemp = get_outside_temperature("Kosice")
            if outsideTemp is None:
                outsideTemp = 0
            print("Outside TEMP ", outsideTemp)
            monitor_temperature_condition(outsideTemp, insideTemp)
            document = {
                "outside": outsideTemp,
                "inside": insideTemp,
                "humidity": humidity,
                "timestamp": int(now.timestamp()),
                "datetime": now.strftime(MONGO_DATETIME_FORMAT),
            }
            database.get_collection(collectionName).insert_one(document)
        elif collectionName == "Socket":
            #get values from payload
            consumed_energy = payload.get('energy')
            consumed_money = consumed_energy * 0.1892 #TODO update tariff via API
            update_or_insert_socket(consumed_energy, consumed_money) 
    except Exception as ex:
        print(ex)

def update_or_insert_socket(new_consumed_energy, new_consumed_money):
    collection = database.get_collection("Socket")
    current_date_str = datetime.now().strftime(MONGO_DATE_FORMAT)
    # Define the query to find a document with the current date
    query = {"date": current_date_str}
    # Try to find a document with the current date
    existing_document = collection.find_one(query)
    if existing_document:
        # If a document with the current date exists, update it
        print(f"Updating existing document for date: {current_date_str}")
        collection.update_one(
            {"_id": existing_document["_id"]}, 
            {"$set": {"consumed_energy": new_consumed_energy, "consumed_money": new_consumed_money}}
        )
    else:
        # If there is no document with the current date, insert a new one
        print(f"Inserting new document for current date: {current_date_str}")
        new_document = {
            "consumed_energy": new_consumed_energy,
            "consumed_money": new_consumed_money,
            "date": current_date_str
        }
        collection.insert_one(new_document)

def get_inside_temp_from_db():
    collection = database.get_collection("Temperature")
    query = {}
    # Sort the documents by date in descending order to get the latest one first
    sort_order = [("date", -1)]
    latest_document = collection.find_one(query, sort=sort_order)
    if latest_document:
        parameter_value = latest_document.get("inside")
        if parameter_value is not None:
            return parameter_value
        else:
            return 0

def get_humidity_from_db():
    collection = database.get_collection("Temperature")
    query = {}
    sort_order = [("date", -1)]
    latest_document = collection.find_one(query, sort=sort_order)
    if latest_document:
        parameter_value = latest_document.get("humidity")
        if parameter_value is not None:
            return parameter_value
        else:
            return 0