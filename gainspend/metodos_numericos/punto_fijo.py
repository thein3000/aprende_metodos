from math import *

def function_fx(equation,x):
    evaluation = eval(equation)
    return evaluation

def metodo_punto_fijo(equation):
    # print(f'equation: {equation}')
    x = 0 #initial_point
    error = 1
    i = 0
    while error > 0.0000099999 and i <= 200:
        next_x = function_fx(equation, x)
        error = abs(next_x - x)
        # print(f'x: {next_x}')
        # print(f'i: {i}')
        # print(f'error: {error}')
        x = next_x
        i += 1
    if i == 200:
        return "No hay solucion"
    else:
        return next_x

# equation = "(e**x - 2) / 2"
# metodo_punto_fijo(equation)
