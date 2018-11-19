from math import *
# equaciont = "2*s*t-y"
# yt = 1.1
# st = 1.2
# ht = .2

def ecuacionordensuperior(equeacion,s,y,t):
    return round(eval(equeacion),6)

def metodo_runge_kutta_de_orden_superior(ecuacion,y,s,h):
    i = 0
    t0 = 0
    while i<2:
        k1 = h*s
        m1 = h*(ecuacionordensuperior(ecuacion,s,y,t0))
        combinacion1 =  s+m1
        combinacion2 = y+k1
        k2 = h*combinacion1
        t1 = t0+h
        m2 = h*(ecuacionordensuperior(ecuacion,combinacion1,combinacion2,t1))
        respuesta1 = y+(1/2)*(k1+k2)
        respuesta2 = s+(1/2)*(m1+m2)
        y = respuesta1
        s = respuesta2
        t0 = t1
        i += 1
    return respuesta1,respuesta2

# print(metodo_runge_kutta_de_orden_superior(equaciont,yt,st,ht))
