arquivo =  open('/home/cezar/Área de Trabalho/pycharm/arquivo.txt','w')

arquivo.write("666 e a lei\nOlá Mundo\n")

for i in range(0,100):
    arquivo.write("numero: "+str(i)+"\n")


