from pymongo import MongoClient

client = MongoClient('MongoDBConnectionString')

# db = client.admin
# serverStatusResult = db.command('serverStatus')
# pprint(serverStatusResult)

db = client.MongoDB
print(f'db = {db.name}')
collection = db.collection
print(f'collection = {collection.name}')

document = {'x': 1}

print(f'document = {document}')
# collection.insert_one(document)

print(f'find_one: {collection.find_one({"key": "value"})}')

print(f'count: {collection.find({"key": "variable"}).count()}')
print(f'count: {collection.count_documents({})}')

for i in collection.find({}):
    print(i)

print(f'kroos: {db.kroos.find({})}')  # sets cursor to mongodb object
for i in db.kroos.find():
    print(i)

blushed = db.kroos.find_one({'_id': 1})
blushed_val = blushed['blushed']  # value of blushed
print(blushed)
print(blushed_val)
