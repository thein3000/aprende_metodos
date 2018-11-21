from random import *
from math import *

def g(t,x):
    return eval(t)

def metodo_punto_fijo(ecuacion):
    p0=0
    i=1
    while i<=100:
        p=g(ecuacion,p0)
        if abs(p-p0)<.001:
            respuesta = p
            break
        i=i+1
        p0=p
        if i>100:
            respuesta = "No hay solucion"
    return respuesta
#
# print(metodo_punto_fijo())
