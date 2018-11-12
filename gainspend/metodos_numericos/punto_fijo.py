from math import *

def function_fx(equation,x):
    evaluation = eval(equation)
    return evaluation

def metodo_punto_fijo(equation):
    x = 0 #initial_point
    error = 1
    i = 0
    while error > 0.00000:
        next_x = function_fx(equation, x)
        error = abs(next_x - x)
        x = next_x
        if i == 200:
            return "No hay solucion"
        i += 1
    # print(next_x)
    return next_x

# equation = "(e**x - 2) / 2"
# metodo_punto_fijo(equation)
