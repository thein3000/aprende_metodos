def parsed_equation(equation):
    equation = equation.replace("**", "^")
    equation = equation.replace("*","")
    equation = equation.replace("sin","sen")
    equation = equation.replace("log","ln")
    # equation = equation.replace("s","y'")
    return equation

def var_value(value):
    value_type = type(value)
    print(value_type)
    if value_type == type(1.5):
        intermediary = float(value)
    elif value_type == type([1,2,3]):
        intermediary = list(value)
    elif value_type == type(2):
        intermediary = int(value)
    else:
        intermediary = value
    return intermediary
