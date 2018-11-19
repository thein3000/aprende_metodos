def parsed_equation(equation):
    equation = equation.replace("**", "^")
    equation = equation.replace("*","")
    equation = equation.replace("sin","sen")
    equation = equation.replace("s","y'")
    return equation
