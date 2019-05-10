'''
nomes = ['aureo','cezar',666,6+6]

for i in range(len(nomes)):
    print(nomes)
    nomes.append('OII')
print(nomes)

for v in range(3):
    print(v)


i = 0

while i <= 10:
    print('i ainda é menor que 10: ',i)
    i = i + 1
'''

x = 1
while x <= 10:
    print(x)
    x = x + x
    if x == 5:
        break
    else:
        print(x)
