import sys

argumntos = sys.argv

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n1

if argumntos[1] == "soma":
    resp = soma(float(argumntos[2]), float(argumntos[3]))
elif argumntos[1] == "sub":
    resp = sub(float(argumntos[2]),float(argumntos[3]))

print(resp)