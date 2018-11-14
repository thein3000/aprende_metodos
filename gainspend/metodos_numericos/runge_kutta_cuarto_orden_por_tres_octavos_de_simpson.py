from math import *
equaciondeveras = "-y/((y**2)+t)"
yodeveras = 1
hdeveras = .5


def equacion4orden3(equeacion,y,t):
    return round(eval(equeacion),8)

def runge_kutta_cuarto_orden_por_tres_octavos_de_simpson(equacion,y0,h):
    i = 0
    t0 = 0
    while i<2:
        k1 = h*(equacion4orden3(equacion,y0,t0))
        y1 = y0+k1/3
        t1 = t0+(h/3)
        k2 = h*(equacion4orden3(equacion,y1,t1))
        y2 = y0+k1/3+k2/3
        t2 = t0+2*h/3
        k3 = h*(equacion4orden3(equacion,y2,t2))
        y3 = y0+k1-k2+k3
        t3= t0+h
        k4 = h*(equacion4orden3(equacion,y3,t3))
        respuesta = y0+(1/8)*(k1+(3*k2)+(3*k3)+k4)
        y0 = respuesta
        t0 = t0+h
        i += 1
    return respuesta

print(runge_kutta_cuarto_orden_por_tres_octavos_de_simpson(equaciondeveras,yodeveras,hdeveras))
#print(equacion4orden3(equaciondeveras,yodeveras,2))
