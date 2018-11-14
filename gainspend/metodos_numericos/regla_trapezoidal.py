from math import *
# integral = "1/(1+x**2)"
# n = 4
# a = 2
# b= 3
#integral = "(sin(2x)+x**3)"
#n = 5
#a = 0
#b= 1
#integral = "(cos(x)+x**2)"
#n = 3
#a = 1
#b= 2

def integracion(temp,x):
    return round(eval(temp),8)

def metodo_regla_trapezoidal(func,s,a0,b0):
    h = (b0-a0)/s
    i = 1
    iteracion = 0
    while i<=n:
        iteracion =iteracion + integracion(func,(a0+i*h))
        i+=1
    respuesta = (h/2)*((integracion(func,a0)+(2*iteracion)))
    return respuesta
print(reglatrapecio(integral,n,a,b))
