import numpy as np

def metodo_montante(Matriz):
    Sols = []
    longitud_renglon = len(Matriz[0])
    for renglon in Matriz:
        Sols.append(renglon[longitud_renglon - 1])
    Matriz = Matriz[:,:-1]
    print(Matriz)
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
