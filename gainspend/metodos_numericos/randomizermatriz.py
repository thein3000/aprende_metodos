import numpy as np
import random

def randomizer():
    valor = random.randint(3,6)
    valor1 = valor+1
    multi = valor1*valor
    x = np.random.randint(multi, size=(valor,valor1))
    return x

print(randomizer())
