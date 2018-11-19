from random import *

def superiorrandom(modo):
    valor1 = randint(1,10)
    if modo == 1:
        #s siendo la derivada de y
        lista = ["y*sin(t)","s*con(t)","s","s*y","y*s","s*y**2","s*y**3","s**2","s**3","sin(s)","s*sin(y)","s*sin(t)","y*cos(t)"]
        valor2 = choice(lista)
        valor5 = choice(lista)
    else:
        lista = ["y","y*t","y/t","(y*t)/2","(s*t)/5","(y*t)/3","y*3","e**t","e**-t","t","t**2","sin(t)","cos(t)","sin(y)","cos(y)"]
        valor2 = choice(lista)
        valor5 = choice(lista)
    signo = ["+","-"]
    valor3 = choice(signo)
    valor4 = randint(1,10)
    ecuacion = str(valor1)+"*"+valor2+valor3+str(valor4)+"*"+valor5
    y0 = round(uniform(0,10),2)
    y1 = round(uniform(0,10),2) #seria y1 en euler o y' en orden superior
    h = round(uniform(0,1),2)
    return ecuacion,y0,y1,h

print(superiorrandom(1))
