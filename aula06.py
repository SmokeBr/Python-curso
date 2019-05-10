lista = [0,1,2,3]
tupla = ('cezar','dia bom')
dicionario = {'nome':'aureo','idade':28}
conjunto = {'cezar','razec'}

print(lista,tupla,dicionario,conjunto)

for a in tupla:
    print(a)

if 'cezar' in conjunto:
    print('cezar esta na coleção')

print(dicionario['nome'])

if 'aureo' in dicionario.values():
    print('eu to no dicionario !!!')

conjunto.add('bolo')
print(conjunto)

if 'bolo' in conjunto:
    print('Oba tem bolo')