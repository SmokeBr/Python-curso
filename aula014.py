import re
import requests

requisicao = requests.get('https://www.valor.com.br/atendimento/fale')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrao não encontrado')
