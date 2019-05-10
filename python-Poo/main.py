from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa',6,'ford',100,)
print('caminhao rosa')
print('Cor: ', caminhao_rosa.cor)
print('Marca: ', caminhao_rosa.marca)
print('Tanque', caminhao_rosa.tanque)
print()
print('carro azul')
carro_azul = Carro('Azul','bmw',30)
print('Cor: ', carro_azul.cor)
print('Marca: ', carro_azul.marca)
print('Tanque', carro_azul.tanque)
carro_azul.abastecer(135)
carro_azul.abastecer(400)
print('Tanque',carro_azul.tanque)

caminhao_rosa.abastecer(110)
print('Tanque',caminhao_rosa.tanque)
