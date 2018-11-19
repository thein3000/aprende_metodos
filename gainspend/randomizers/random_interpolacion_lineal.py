from random import *

def generate_interpolacion_lineal():
    listax= []
    listay = []
    valor1x = randint(1,10)
    valor2x = randint(11,20)
    valor1y = uniform(0,10)
    valor2y = uniform(valor1y+1,12)
    listax.append(valor1x)
    listax.append(valor2x)
    listay.append(valor1y)
    listay.append(valor2y)
    valort = randint(valor1x+1,valor2x-1)
    return listax,listay,valort

# print(randomlineal())
