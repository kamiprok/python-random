import requests
import json

response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')

print(response.text)

to_dict = json.loads(response.text)

print(to_dict)
print(f'"{to_dict["quote"]}" - {to_dict["author"]}')
