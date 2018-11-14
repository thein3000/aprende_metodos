from math import *
#integral = "(3*x**3)-10"
#n = 4
#a = -2
#b= 2
# integral = "1/(1+x**2)"
# n = 10
# a = 2
# b= 3
#integral = "(cos(x)+x**2)"
#n = 3
#a = 1
#b= 2


def integracionna(temp,x):
    return round(eval(temp),8)

def ciclo(temp,h0,valora,valorn):
    iteracion = 0
    i = 1
    while i<valorn:
        if i%2 == 0:
            iteracion = iteracion +4*(integracionna(temp,(valora+i*h0)))
        else:
            iteracion = iteracion +2*(integracionna(temp,(valora+i*h0)))
        i += 1
    return iteracion


def metodo_regla_un_tercio_de_simpson(ecuacion,a0,b0,n0):
    h = (b0-a0)/n0
    simpsonvalor = ciclo(ecuacion,h,a0,n0)
    respuesta = (h/3)*(integracionna(ecuacion,a0)+simpsonvalor+integracionna(ecuacion,b0))
    return respuesta



# print(metodo_regla_un_tercio_de_simpson(integral,a,b,n))
