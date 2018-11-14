from math import *
# integral = "(3*x**3)-10"
# n = 4
# a = -2
# b= 2
#integral = "(sin(2x)+x**3)"
#n = 5
#a = 0
#b= 1
#integral = "(cos(x)+x**2)"
#n = 3
#a = 1
#b= 2


def integracionna(temp,x):
    return round(eval(temp),8)

def iteracionescotas(temp,h0,valora,labiertas):
    iteracion = 0
    for i, j in enumerate(labiertas, start=0):
        iteracion = iteracion+j*(integracionna(temp,(valora+(i*h0))))
    return iteracion


def metodo_newton_cotes_abiertas(ecuacion,a0,b0,n0):
    alphas=[3/2,4/3,5/24,6/20,7/1440,8/945]
    n1=[0,1,1,0]
    n2=[0,2,-1,2,0]
    n3=[0,11,1,1,11,0]
    n4=[0,11,-14,26,-14,11,0]
    n5=[0,611,-453,562,562,-453,611,0]
    n6=[0,460,-954,2196,-2459,2196,-954,460,0]
    h = (b0-a0)/(n+2)
    if n==6:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n6)
    elif n==5:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n5)
    elif n==4:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n4)
    elif n==3:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n3)
    elif n==2:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n2)
    else:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n1)
    respuesta = alphas[n-1]*h*iteracioncotas
    return respuesta



# print(metodo_newton_cotes_abiertas(integral,a,b,n))
