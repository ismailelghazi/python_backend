from pymongo import MongoClient

client = MongoClient("mongodb+srv://ismail47el:BoAM6I7skfK7o1hj@assurance.gcuvjlw.mongodb.net/?retryWrites=true&w=majority&appName=assurance")

db = client.assurance_prj

collection_name = db["Client_collection"]