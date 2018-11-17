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


def metodo_newton_cotes_cerradas(ecuacion,a0,b0,n0):
    alphas=[1/2,1/3,3/8,2/45,5/288,1/140,7/17280,14/14145,9/89600,5/299376]
    n1=[1,1]
    n2=[1,4,1]
    n3=[1,3,3,1]
    n4=[7,32,12,32,7]
    n5=[19,75,50,50,75,19]
    n6=[41,216,27,272,27,216,41]
    n7 = [751,3577,1323,2989,2989,1323,3577,751]
    n8 = [989,5888,-928,10946,-4540,10946,-928,5888,989]
    n9 = [2857,15741,1080,19344,5788,5788,19344,1080,15741,2857]
    n10 = [16067,106300,-48525,272400,-260550,427368,-260550,272400,-48525,106300,16067]
    h = (b0-a0)/(n0)
    if n0==10:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n10)
    elif n0==9:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n9)
    elif n0==8:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n8)
    elif n0==7:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n7)
    elif n0==6:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n6)
    elif n0==5:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n5)
    elif n0==4:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n4)
    elif n0==3:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n3)
    elif n0==2:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n2)
    else:
        iteracioncotas = iteracionescotas(ecuacion,h,a0,n1)
    respuesta = alphas[n0-1]*h*iteracioncotas
    return respuesta



# print(metodo_newton_cotes_cerradas(integral,a,b,n))
