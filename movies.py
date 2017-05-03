import requests
import json

url = 'http://www.omdbapi.com/?t=Game+of+thrones'

r = requests.get(url,'')
d = r.json()

print(d["Title"])
print(d)
