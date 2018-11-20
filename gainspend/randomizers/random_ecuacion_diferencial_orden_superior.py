from random import *

def generate_ecuacion_diferencial_orden_superior(modo):
    valor1 = randint(1,10)
    if modo == 1:
        #s siendo la derivada de y
        lista = ["y*sin(t)","z*con(t)","z","z*y","y*z","z*y**2","z*y**3","z**2","z**3","sin(z)","z*sin(y)","z*sin(t)","y*cos(t)"]
        valor2 = choice(lista)
        valor5 = choice(lista)
    else:
        lista = ["y","y*t","y/t","(y*t)/2","(y*t)/3","y*3","e**t","e**-t","t","t**2","sin(t)","cos(t)","sin(y)","cos(y)"]
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

# print(generate_ecuacion_diferencial_orden_superior(1))
