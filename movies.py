import requests
import json

url = 'http://www.omdbapi.com/?t=Rambo'

r = requests.get(url,'')
d = r.json()

print(d["Title"])
print(d)
