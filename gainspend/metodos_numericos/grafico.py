from math import *
#ecuacion = "(x**4)-(6.5*x**2)+2"
def metodo_grafico(t):
    x = [-3,-2,-1,0,1,2,3]
    for i in x:
        resultado = evaluar(t,i)
        print (resultado)
    return resultado

def evaluar(ecuacion1,x):
    return eval(ecuacion1)

# print(metodo_Grafico(ecuacion))
