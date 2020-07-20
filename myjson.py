import json

# some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

x = {'data': [{'name': 'John', 'age': 30, 'city': 'New York'}]}

# parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y['age'])

with open('data.json', 'w') as file:
    json.dump(x, file, indent=4)

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

print(json.dumps(x, indent=4))
