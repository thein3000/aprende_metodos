import numpy as np
import random

def generate_matriz():
    # valor = random.randint(3,6)
    valor = 3
    valor1 = valor+1
    multi = valor1*valor
    x = np.random.randint(multi, size=(valor,valor1))
    return x

# print(generate_matriz())
