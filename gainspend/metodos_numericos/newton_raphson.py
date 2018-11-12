def function_fx(equation,x):
    evaluation = eval(equation)
    return evaluation

def derivative_fx(equation,x):
    h = 0.000001
    derivative = (function_fx(equation,x + h) - function_fx(equation,x)) / h
    return derivative

def raphson_formula(equation, x):
    derivative = derivative_fx(equation, x)
    function = function_fx(equation, x)
    return x - (function/derivative)

def metodo_newton_raphson(equation):
    x = 1 #initial_point
    error = 1
    i = 0
    while error > 0.00000:
        if i != 0:
            x = next_x
        next_x = raphson_formula(equation, x)
        error = abs(next_x - x)
        i += 1
    return next_x

# equation="0.8*x**2 + x - 3"
# metodo_newton_raphson(equation)
