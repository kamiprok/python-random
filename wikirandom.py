import requests

response = requests.get('https://en.wikipedia.org/wiki/Special:Random')

print(response.url)
