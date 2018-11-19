from random import *

def generate_ecuacion_diferencial():
    valor1 = randint(1,10)
    lista = ["y","y*t","y/t","(y*t)/2","(y*t)/5","(y*t)/3","y*3","e**t","e**-t","t","t**2","sin(t)","cos(t)","sin(y)","cos(y)"]
    valor2 = choice(lista)
    signo = ["+","-"]
    valor3 = choice(signo)
    valor4 = randint(1,10)
    valor5 = choice(lista)
    ecuacion = str(valor1)+"*"+valor2+valor3+str(valor4)+"*"+valor5
    y0 = round(uniform(0,10),2)
    h0 = round(uniform(0,1),2)
    return ecuacion,y0,h0

# print(generate_ecuacion_diferencial())
