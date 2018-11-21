from random import *

def generate_grafico():
    valor1 = randint(1,15)
    lista = ["x**4","x**3","x**2","x","5/x"]
    valor2 = choice(lista)
    signo = ["+","-"]
    valor3 = choice(signo)
    valor4 = randint(1,15)
    valor5 = choice(lista)
    ecuacion = "("+str(valor1)+"*"+valor2+")"+valor3+"("+str(valor4)+"*"+valor5+")"
    return ecuacion

# print(random_grafico())

