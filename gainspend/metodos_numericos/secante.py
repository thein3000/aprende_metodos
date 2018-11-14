from math import *

def fx(equation,x):
    return eval(equation)

def secante_formula(equation,x_pre,x_act):
    return x_act - ((fx(equation,x_act)*(x_act-x_pre))) / (fx(equation,x_act) - fx(equation,x_pre))

def metodo_secante(equation):
    error = 1
    i = 0
    x_pre = 0
    x_act = 1
    while error > 0.001:
        if i == 0:
            x_mem = x_act
            x_act = secante_formula(equation,x_pre,x_act)
            x_pre = x_mem
        else:
            x_mem = x_act
            x_act = secante_formula(equation,x_pre,x_act)
            x_pre = x_mem
            error = abs(x_act - x_pre)
        if i == 200:
            return "No hay solucion"
        i += 1
    # print(x_act)
    return x_act

# equation = "2*x**2 - 6*x - 2"
# equation = "x*e**x - 10"
# equation="e**(-x) - x"
# metodo_secante(equation)
