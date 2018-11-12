
import numpy as np
# define matrix A using Numpy arrays
#
# A = [
#     [3, 1, 1],
#     [1, 4, 1],
#     [1, 1, 6]
#     ]
# B = [1, 2, 3]

# C = [
#     [3, 1, 1, 1],
#     [1, 4, 1, 2],
#     [1, 1, 6, 3]
#     ]

def metodo_montante(Matriz):
    Sols = []
    longitud_renglon = len(Matriz[0])
    for renglon in Matriz:
        Sols.append(renglon[longitud_renglon - 1])
        del renglon[longitud_renglon - 1]
    print(Matriz)
    print(Sols)
    Matriz = np.array(Matriz)
    Sols = np.array(Sols)
    try:
        respuesta = np.linalg.solve(Matriz, Sols )
    except np.linalg.LinAlgError as e:
        if 'Singular matrix' in str(e):
            respuesta = "No hay solucion"
            return respuesta, respuesta, respuesta
        else:
            raise
    # return respuesta
    return respuesta[0], respuesta[1], respuesta[2]

# x,y,z = metodo_montante(C)
# print(x)
# print(y)
# print(z)

# print(solucionarmatriz(A,B)[0])
# print(type(solucionarmatriz(A,B)))
