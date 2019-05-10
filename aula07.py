def soma(numero1,numero2):
    resp =  numero1 + numero2
    return resp

restorno = soma(5,1)
print(restorno)

def tem_sete_letras(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
if tem_sete_letras('1234567'):
    print('realemnte tem sete letras')
