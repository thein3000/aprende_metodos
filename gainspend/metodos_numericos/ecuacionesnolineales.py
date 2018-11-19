from random import *

def randomizerlineal():
    list = ["x**2","x","x**3","sin(x)","cos(x)","ln(x)","e**x","**x","x","x*e","x**1/2","1/x","(x**2)/5"]
    valor1 = round(uniform(-10.0,10.0),2)
    valor2 = choice(list)
    valor3 = round(uniform(-10.0,10.0),2)
    signo = ["+","-"]
    valor4 = choice(list)
    valor5 = choice(signo)
    ecuacion = str(valor1)+"*"+valor2+valor5+str(valor3)+"*"+valor4
    return ecuacion

print(randomizerlineal())
