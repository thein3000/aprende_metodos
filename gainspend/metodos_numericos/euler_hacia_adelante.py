from math import *
# equaciondeveras = "(5*y*t-1)/3"
# yodeveras = 2
# hdeveras = .2


def equacionmoveradelante(equeacion,y,t):
    return eval(equeacion)


def metodo_euler_hacia_adelante(equeacion1,y0,h):
    i = 0
    t0 = 0
    parte1 = equacionmoveradelante(equeacion1,y0,t0)
    respuesta = y0+(h*parte1)
    y0 = respuesta
    parte2 = equacionmoveradelante(equeacion1,y0,h)
    parte3 = h*parte2
    respuesta = y0+parte3
    return respuesta




# print(euler_hacia_adelante(equaciondeveras,yodeveras,hdeveras))
