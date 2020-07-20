from pymongo import MongoClient
from pprint import pprint
from getpass import getpass

# dbpass = getpass('dbpass: ')

client = MongoClient('MongoDBConnectionString')

# db = client.admin
# serverStatusResult = db.command('serverStatus')
# pprint(serverStatusResult)

db = client.MongoDB
pprint(f'db = {db}')
collection = db.collection
pprint(f'collection = {collection}')
document = {
    'key': 'value'
}
pprint(f'document = {document}')
# collection.insert_one(document)

pprint(f'find_one: {db.collection.find_one({"key": "value"})}')
pprint(f'collection_names: {db.collection_names}')
pprint(f'count: {db.collection.find({"key": "variable"}).count()}')
pprint(f'kroos: {db.kroos.find({})}')  # sets cursor to mongodb object
for i in db.kroos.find():
    print(i)
blushed = db.kroos.find_one({'_id': '1'})
blushed_val = blushed['blushed']  # value of blushed
print(blushed_val)
blushed_val += 1
print(blushed_val)
db.kroos.find_one_and_update({'_id': '1'}, {'$inc': {'blushed': 1}})
blushed = db.kroos.find_one({'_id': '1'})
pprint(blushed)
