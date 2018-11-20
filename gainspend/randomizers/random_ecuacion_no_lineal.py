from random import *

def generate_ecuacion_no_lineal():
    list = ["x**2","x","x**3","sin(x)","cos(x)","log(x)","e**x","*x","x","x*e","1/x","(x**2)/5"]
    valor1 = randrange(1,10)#round(uniform(1,10),0)
    valor2 = choice(list)
    valor3 = randrange(1,10)#round(uniform(1,10),0)
    signo = ["+","-"]
    valor4 = choice(list)
    valor5 = choice(signo)
    ecuacion = str(valor1)+"*"+valor2+valor5+str(valor3)+"*"+valor4
    return ecuacion

# print(generate_ecuacion_no_lineal())
