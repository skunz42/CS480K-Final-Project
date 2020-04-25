import pymongo

print("Connecting...")
client = pymongo.MongoClient("mongodb+srv://emoelle2:watson@cs480kfp-xgix9.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.CS480KFP
collection = db.stores

print(collection.find_one())
