from math import *
equaciondeveras = "(y+t)**2/(1-y)"
yodeveras = .4
hdeveras = .2


def equacion4orden(equeacion,y,t):
    return round(eval(equeacion),8)

def runge_kutta_cuarto_orden_por_un_tercio_de_simpson(equacion,y0,h):
    i = 0
    t0 = 0
    while i<2:
        k1 = h*(equacion4orden(equacion,y0,t0))
        y1 = y0+k1/2
        t1 = t0+(h/2)
        k2 = h*(equacion4orden(equacion,y1,t1))
        y2 = y0+k2/2
        t2 = t0+h/2
        k3 = h*(equacion4orden(equacion,y2,t2))
        y3 = y0+k3
        t3= t0+h
        k4 = h*(equacion4orden(equacion,y3,t3))
        respuesta = y0+(1/6)*(k1+(2*k2)+(2*k3)+k4)
        y0 = respuesta
        t0 = t0+h
        i += 1
    return respuesta

print(runge_kutta_cuarto_orden_por_un_tercio_de_simpson(equaciondeveras,yodeveras,hdeveras))
