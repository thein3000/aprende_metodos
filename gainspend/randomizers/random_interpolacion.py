from random import *

def generate_interpolacion(modo):
    listax = []
    listay = []
    if modo == 1:
        #Este es para impares(lagrange,diferencias)
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
        valort = round(uniform(listax[0],listax[i-2]),2)
    else:
        # para pares (newton_hacia adelante y atras)
        valortotal = randint(3,7)
        valorx = round(uniform(1,10),2)
        intervalor = round(uniform(1,2),2)
        listax.append(valorx)
        i = 2
        while i<=valortotal:
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
        valort = round(uniform(listax[0],listax[i-2]),2)
    return valort,listax,listay

# print(generate_interpolacion(1))
