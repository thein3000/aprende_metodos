from math import *
from random import *
import numpy as np

# t = "cos(x)"
# x0 = [1.1,1.9,2.4,4.8]
# y0 = [2.5,2.7,3.7,5.2]

def metodo_cuadratica_con_funcion(x,y,ecuacion):
    lista_x = np.array(x)
    lista_y = np.array(y)
    lista_coeficientes = []
    matrix = generar_matriz(lista_x,lista_y,ecuacion)
    resultados= metodo_montante(matrix)
    #print(matrix)
    return resultados
    #return "te"

def generar_matriz(list_x,list_y,ecuacion1):
    x_sums = []
    xy_sums = []
    fx_sums = []
    ifx_sums = []
    matriz = []
    n = len(list_x)
    amount_of_sums = 4
    amount_of_rows = 4
    amoutn_of_columns = 5
    for i in range(1,amount_of_sums+1):
        x_sums.append(sum_at_nth_power(list_x,i))
    #print(x_sums)
    for i in range(0,(amount_of_rows-1)):
        xy_sums.append(sum_at_nth_power_times_n(list_x,list_y,i))
    #print(xy_sums)
    for i in range(1,(amount_of_rows-1)):
        fx_sums.append(sum_at_nth_power_function(list_x,ecuacion1,i))
    #print(fx_sums)
    for i in range(1,amount_of_rows):
        ifx_sums.append(num_at_nth_power_times_y_or_x(list_x,list_y,ecuacion1,i))
    #print(ifx_sums)
    for row in range(0,4): #For all rows in matrix
        starting_power = row # Determines on which element of x_sums will the appending start for each row
        row_buffer=[]
        for col in range(0,5): #For all but the last column
            if row == 0 and col == 0:
                row_buffer.append(n)
            elif row==0 and col ==1:
                row_buffer.append(x_sums[0])
            elif row==0 and col ==2:
                row_buffer.append(x_sums[1])
            elif row==0 and col ==3:
                row_buffer.append(fx_sums[0])
            elif row==0 and col ==4:
                row_buffer.append(xy_sums[0])
            elif row==1 and col ==0:
                row_buffer.append(x_sums[0])
            elif row==1 and col ==1:
                row_buffer.append(x_sums[1])
            elif row==1 and col ==2:
                row_buffer.append(x_sums[2])
            elif row==1 and col ==3:
                row_buffer.append(ifx_sums[0])
            elif row==1 and col ==4:
                row_buffer.append(xy_sums[1])
            if row == 2 and col == 0:
                row_buffer.append(x_sums[1])
            elif row==2 and col ==1:
                row_buffer.append(x_sums[2])
            elif row==2 and col ==2:
                row_buffer.append(x_sums[3])
            elif row==2 and col ==3:
                row_buffer.append(ifx_sums[1])
            elif row==2 and col ==4:
                row_buffer.append(xy_sums[2])
            elif row==3 and col ==0:
                row_buffer.append(fx_sums[0])
            elif row==3 and col ==1:
                row_buffer.append(ifx_sums[0])
            elif row==3 and col ==2:
                row_buffer.append(ifx_sums[1])
            elif row==3 and col ==3:
                row_buffer.append(fx_sums[1])
            elif row==3 and col== 4:
                row_buffer.append(ifx_sums[2])

        matriz.append(row_buffer)
    return matriz

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

def sum_at_nth_power_function(list_x,ecuacion,power):
    sum = 0
    for number in list_x:
        sum = sum + pow(ecuacionmetodo(ecuacion,number),power)
    return sum

def num_at_nth_power_times_y_or_x(list_x,list_y,ecuacion,j):
        sum = 0
        joined_list = zip(list_x,list_y)
        if j == 3:
            for first_num, second_num in joined_list:
                sum = sum + ecuacionmetodo(ecuacion,first_num) * second_num
        else:
            for numero in list_x:
                sum = sum + ecuacionmetodo(ecuacion,numero) * pow(numero,j)
        return sum

def ecuacionmetodo(temp,x):
    respuesta = eval(temp)
    return respuesta

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

# print(minimos_cuadrados_lineal_funcion(x0,y0,t))
