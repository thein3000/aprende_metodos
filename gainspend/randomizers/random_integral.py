from random import *

def generate_integral(modo):
    valor1 = randint(1,10)
    list = ["1/1-x**2","x**2","x**3","e**x"]
    valor2 = choice(list)
    signo = ["+","-"]
    valor3 = choice(signo)
    valor4 = randint(1,20)
    ecuacion = str(valor1)+"*"+valor2+valor3+str(valor4)
    valora = randint(-2,2)
    valorb = randint(2,4)
    if modo == 1:
        #trapezoide
        valorn = randint(3,10)
    elif modo == 2:
        #cotes abiertas
        valorn = randint(1,6)
    elif modo == 3:
        #cotes cerradas
        valorn = randint(1,10)
    elif modo == 4:
        # 1/3 simpsonvalor
        lista = [2,4,6,8,10]
        valorn = choice(lista)
    else:
        #3/8 simpson
        lista = [1,3,5,7,9]
        valorn = choice(lista)
    return ecuacion,valora,valorb,valorn

# print(generate_integral(5))
