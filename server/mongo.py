# import json
# from services import *
# from datetime import datetime
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://danilbond49:maker@cluster0.6h6gsaf.mongodb.net/?retryWrites=true&w=majority"
# MONGO_DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"
# MONGO_DATE_FORMAT = "%d/%m/%Y"

# # Set the Stable API version when creating a new client
# client = MongoClient(uri, server_api=ServerApi('1'))
# database = client.get_database("MQTTDB")

# def process_data(collectionName, payload):
#     collection = database.get_collection(collectionName)
#     now = datetime.now()
#     try:
#         if collectionName == "Temperature":
#             insideTemp = payload.get('temperature')
#             outsideTemp = get_outside_temperature("Kosice")
#             if outsideTemp is None:
#                 outsideTemp = 0
#             print("Outside TEMP ", outsideTemp)
#             shouldSendTemperatureAllert(outsideTemp, insideTemp)
#             document = {
#                 "outside": outsideTemp,
#                 "inside": insideTemp,
#                 "timestamp": int(now.timestamp()),
#                 "datetime": now.strftime(MONGO_DATETIME_FORMAT),
#             }
#             collection.insert_one(document)
#         elif collectionName == "Socket":
#             #get values from payload
#             update_or_insert_socket() 
#     except Exception as ex:
#         print(ex)

# def update_or_insert_socket(online_time_increment):
#     collection = database.get_collection("Socket")
#     current_date_str = datetime.now().strftime(MONGO_DATE_FORMAT)
#     # Define the query to find a document with the current date
#     query = {"date": current_date_str}
#     # Try to find a document with the current date
#     existing_document = collection.find_one(query)
#     if existing_document:
#         # If a document with the current date exists, update it
#         print(f"Updating existing document for date: {current_date_str}")
#         new_online_time = existing_document["online_time"] + online_time_increment
#         collection.update_one({"_id": existing_document["_id"]}, {"$set": {"online_time": new_online_time}})
#     else:
#         # If there is no document with the current date, insert a new one
#         print(f"Inserting new document for date: {current_date_str}")
#         new_document = {
#             "online_time": online_time_increment,
#             "consumed_volts": 0,  # Modify as needed
#             "consumed_money": 0,  # Modify as needed
#             "date": current_date_str
#         }
#         collection.insert_one(new_document)