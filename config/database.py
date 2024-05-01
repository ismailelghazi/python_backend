from pymongo import MongoClient

client = MongoClient("mongodb+srv://ismail47el:<password>@assurance.gcuvjlw.mongodb.net/?retryWrites=true&w=majority&appName=assurance")

db = client.assurance_prj

collection_name = db("Clint_collection")
