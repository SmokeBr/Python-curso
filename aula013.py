import requests
import json

req = None
try:
    req = requests.get('http://facebook.com')
except:
    print('erro')
    exit()

print(req.text)

dicionario = json.loads(req.text)
print(dicionario)
