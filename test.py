import requests as rp
import json

r = rp.get('http://127.0.0.1:8000/')
print(json.loads(r.json()))