from math import *

def function_fx(equation,x):
    evaluation = eval(equation)
    return evaluation

def conseguir_ab(equation):
    ab_no_encontrada = True
    lower_bound = -2
    upper_bound = 3
    while ab_no_encontrada:
        for i in range(lower_bound,upper_bound):
            if i == lower_bound:
                fa = function_fx(equation, i)
                if fa >= 0:
                    positive = True
                else:
                    positive = False
            else:
                fa = function_fx(equation, i)
                if fa >= 0:
                    new_positive = True
                else:
                    new_positive = False
                if positive != new_positive:
                    b = i
                    a = i - 1
                    ab_no_encontrada = False
        lower_bound -= 5
        upper_bound += 5
        if lower_bound < -35:
            return "No hay solucion", "No hay solucion"
    return a, b

def formula_falsa_posicion(equation,a,b,fa,fb):
    return a - ((fa*(b - a)) / (fb - fa))

def metodo_falsa_posicion(equation):
    a, b = conseguir_ab(equation)
    if a == "No hay solucion":
        return "No hay solucion"
    fa = function_fx(equation, a)
    fb = function_fx(equation, b)
    error = 1
    i = 0
    while error > 0.001:
        if i == 0:
            next_x = formula_falsa_posicion(equation,a,b,fa,fb)
            a = next_x
            fa = function_fx(equation, a)
            x = next_x
        else:
            next_x = formula_falsa_posicion(equation,a,b,fa,fb)
            a = next_x
            fa = function_fx(equation, a)
            error = abs(next_x - x)
            x = next_x
        if i == 200:
            return "No hay solucion"
        i += 1
    # print(next_x)
    return next_x

# equation = "x*e**x - 10"
# metodo_falsa_posicion(equation)
