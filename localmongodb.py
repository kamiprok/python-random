from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://127.0.0.1:27017')

db = client.MongoDB

print(db)

collection = db.collection

print(collection)

# document = {'x': 3}
# collection.insert_one(document)

# document = {'_id': ObjectId('5f16df88dc717123f2975497')}
# collection.delete_one(document)

for document in collection.find():
    print(document)

# first run mongod.exe with --dbpath to start database
# C:\Program Files\MongoDB\Server\4.2\bin>mongod.exe --dbpath C:\mongodb\data\db\

