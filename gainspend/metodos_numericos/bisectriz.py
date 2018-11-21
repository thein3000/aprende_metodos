import scipy.optimize as opt
import numpy as np

def func(x):
    return np.sin(x)**2+6-x

def metodo_bisectriz(a,b):
    try:
        respuesta = opt.bisect(func,a,b)
    except ValueError as e:
        if 'must have different signs' in str(e):
            respuesta = "No hay solucion"
        else:
            raise
    return respuesta

#print(metodo_bisectriz(6,7))
