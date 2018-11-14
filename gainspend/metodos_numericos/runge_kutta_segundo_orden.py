from math import *
equaciondeveras = "e**(-t)-3*y"
yodeveras = 1
hdeveras = .5

def equacion2orden(equeacion,y,t):
    return round(eval(equeacion),8)

def metodo_runge_kutta_segundo_orden(equacion,y0,h):
    t0 = 0
    k1=h*(equacion2orden(equacion,y0,t0))
    y1 = y0+k1
    t1 = t0+h
    k2=h*(equacion2orden(equacion,y1,t1))
    respuesta = 1+(1/2)*(k2+k1)
    y0 = respuesta
    t0 = t1
    k1=h*(equacion2orden(equacion,y0,t0))
    y1 = y0+k1
    t1 = t0+h
    k2=h*(equacion2orden(equacion,y1,t1))
    respuesta = 1+(1/2)*(k2+k1)
    return respuesta

print(metodo_runge_kutta_segundo_orden(equaciondeveras,yodeveras,hdeveras))
