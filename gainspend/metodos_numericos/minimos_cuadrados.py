import numpy as np

def metodo_minimos_cuadrados(mode,x,y):
    list_x = np.array(x)
    list_y = np.array(y)
    lista_coeficientes = []
    matrix = generar_matriz(mode,list_x,list_y)
    resultados = metodo_montante(matrix)
    # print(resultados)
    return lista_coeficientes

def generar_matriz(mode,list_x,list_y):
    x_sums = []
    xy_sums = []
    matrix = []
    n = len(list_x)
    amount_of_sums = mode * 2
    amount_of_rows = mode + 1
    amount_of_columns = mode + 2
    for i in range(1,amount_of_sums + 1):
        x_sums.append(sum_at_nth_power(list_x,i))
    # print(x_sums)
    for i in range(0,amount_of_rows):
        xy_sums.append(sum_at_nth_power_times_n(list_x,list_y,i))
        # print(xy_sums)
    for row in range(0,amount_of_rows): #For all rows in matrix
        starting_power = row # Determines on which element of x_sums will the appending start for each row
        row_buffer=[]
        for col in range(0,amount_of_columns): #For all but the last column
            if row == 0 and col == 0:
                row_buffer.append(n)
            elif col == amount_of_columns-1:
                row_buffer.append(xy_sums[row])
            else:
                row_buffer.append(x_sums[starting_power+col-1])
        matrix.append(row_buffer)
    # print(matrix)
    return matrix

def sum_at_nth_power(list,power):
    sum = 0
    for number in list:
        sum += pow(number,power)
    return sum

def sum_at_nth_power_times_n(first_list,second_list,power):
    sum = 0
    joined_list = zip(first_list,second_list)
    for first_num, second_num in joined_list:
        sum += pow(first_num,power) * second_num
    return sum

def metodo_montante(Matriz):
    Sols = []
    longitud_renglon = len(Matriz[0])
    for renglon in Matriz:
        Sols.append(renglon[longitud_renglon - 1])
        del renglon[longitud_renglon - 1]
    Matriz = np.array(Matriz)
    Sols = np.array(Sols)
    try:
        respuesta = np.linalg.solve(Matriz, Sols )
    except np.linalg.LinAlgError as e:
        if 'Singular matrix' in str(e):
            respuesta = "No hay solucion"
            return respuesta
        else:
            raise
    # return respuesta
    return respuesta

# # x,y,z = metodo_montante(C)
# x = [
#     1.1,
#     1.9,
#     2.4,
#     4.8,
#     5.1,
#     10.5
# ]
# y = [
#     2.5,
#     2.7,
#     3.7,
#     5.2,
#     6.0,
#     8.3
# ]
# mode = 1
# metodo_minimos_cuadrados(mode,x,y)
