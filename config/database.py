from pymongo import MongoClient

client = MongoClient("mongodb+srv://ismail:Tq5TdjwC8UQFuaDV@cluster0.tol3lhy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.assurance_prj

collection_name = db["Client_collection"]
