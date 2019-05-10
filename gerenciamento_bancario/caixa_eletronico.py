from contas import Contas
from principal import Banco_de_dados

cliente1 = Banco_de_dados('cezar','3333','45','123:345',500.00)
print('conta',cliente1.conta)
print('idade',cliente1.idade)
print('cpf',cliente1.cpf)