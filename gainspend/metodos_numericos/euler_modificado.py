from math import *
# equaciondeveras = "sin(t)-(y/2)"
# yodeveras = 1
# hdeveras = .5
# y1deveras = 1

def equacionmover(equeacion,y,t):
    return eval(equeacion)


def metodo_euler_modificado(equeacion1,y0,h,y1):
    i = 0
    t0 = 0
    t1 = t0+h
    sacarh = h/2
    parte1 = equacionmover(equeacion1,y0,t0)
    parte2 = equacionmover(equeacion1,y1,t1)
    parte3 = round((parte1+parte2),8)
    respuesta = y0+sacarh*parte3
    print(respuesta)
    y0=y1
    y1 = respuesta
    t0 = h
    t1 = t0+h
    sacarh = h/2
    parte1 = equacionmover(equeacion1,y0,t0)
    parte2 = equacionmover(equeacion1,y1,t1)
    parte3 = round((parte1+parte2),8)
    respuesta = y0+sacarh*parte3
    return round(respuesta,8)




# print(euler_modificado(equaciondeveras,yodeveras,hdeveras,y1deveras))
