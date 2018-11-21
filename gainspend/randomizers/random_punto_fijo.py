from random import *

def generate_punto_fijo():
    list= ["0.5*sqrt(10-x**2)","(e**(-x))",".7*sqrt(15-x**2)","14*sqrt(x+1)",".2*e**x",".5**x"]
    ecuacion = choice(list)
    return ecuacion

# print(random_fijo())
