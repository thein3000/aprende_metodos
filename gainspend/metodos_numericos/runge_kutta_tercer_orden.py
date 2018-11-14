from math import *
equaciondeveras = "(((2*y*t)+1)/y**2)"
yodeveras = 1
hdeveras = .25


def equacion3orden(equeacion,y,t):
    return round(eval(equeacion),8)

def metodo_runge_kutta_tercer_orden(equacion,y0,h):
    i = 0
    t0 = 0
    while i<2:
        k1 = h*(equacion3orden(equacion,y0,t0))
        y1 = y0+k1/2
        t1 = t0+(h/2)
        k2 = h*(equacion3orden(equacion,y1,t1))
        y2 = y0-k1+(2*k2)
        t2 = t0+h
        k3 = h*(equacion3orden(equacion,y2,t2))
        respuesta =1+(1/6)*(k1+(4*k2)+k3)
        y0 = respuesta
        t0 = t0+h
        i+=1
    return round(respuesta,8)

print( metodo_runge_kutta_tercer_orden(equaciondeveras,yodeveras,hdeveras))
