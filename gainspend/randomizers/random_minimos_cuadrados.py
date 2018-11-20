from random import *

def generate_minimos_cuadrados():
    listax = []
    listay = []
    valortotal = randint(3,5)
    valorx = round(uniform(1,10),2)
    listax.append(valorx)
    i = 2
    while i<=valortotal:
        intervalor = round(uniform(1,2),2)
        valorx = round(valorx + intervalor,2)
        listax.append(valorx)
        i+=1
    valory = round(uniform(1,10),2)
    listay.append(valory)
    i = 2
    while i<=valortotal:
        intervalor = round(uniform(1,3),2)
        valory = round(valory+intervalor,2)
        listay.append(valory)
        i+=1
    return listax,listay

# print(randomizer())
