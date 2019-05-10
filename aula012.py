import requests

requisicao = requests.get('https://solyd.com.br')

print(type(requisicao))
print(requisicao.status_code)
print(requisicao.text)