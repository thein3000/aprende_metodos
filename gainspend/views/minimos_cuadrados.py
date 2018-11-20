from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from gainspend.custom_helpers import var_value, parsed_equation
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.metodos_numericos import minimos_cuadrados_general
from gainspend.metodos_numericos import lineal_con_funcion
from gainspend.randomizers import random_minimos_cuadrados
from gainspend.randomizers import random_minimos_cuadrados_con_funcion
# import numpy as np

@login_required
def preface_linea_recta(request):
    method = Method.objects.filter(name="Línea Recta").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_linea_recta.html', context)

@login_required
def excercise_linea_recta(request):
    method = Method.objects.filter(name="Línea Recta").first()
    # Variables del problema
    mode = 1
    invalid = True
    while invalid:
        try:
            x,y = random_minimos_cuadrados.generate_minimos_cuadrados()
            x_print = var_value(x)
            y_print = var_value(y)
            lista_coeficientes = minimos_cuadrados_general.metodo_minimos_cuadrados(mode,x,y)
            invalid = False
        except Exception as e:
            print(e)
            invalid = True
    # print(f'Resultado minimos: {lista_coeficientes}')
    # Variables de presentacion del problema
    xy_print = zip(x_print,y_print)
    if type(lista_coeficientes) != type("string"):
        result_a0 = lista_coeficientes[0]
        result_a1 = lista_coeficientes[1]
    else:
        result_a0 = lista_coeficientes
        result_a1 = lista_coeficientes
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "xy_print": xy_print,
        "result_a0": result_a0,
        "result_a1": result_a1,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_linea_recta.html', context)


@login_required
def preface_cuadratica(request):
    method = Method.objects.filter(name="Cuadratica").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_cuadratica.html', context)

@login_required
def excercise_cuadratica(request):
    method = Method.objects.filter(name="Cuadratica").first()
    # Variables del problema
    mode = 2
    invalid = True
    while invalid:
        try:
            x,y = random_minimos_cuadrados.generate_minimos_cuadrados()
            x_print = var_value(x)
            y_print = var_value(y)
            lista_coeficientes = minimos_cuadrados_general.metodo_minimos_cuadrados(mode,x,y)
            invalid = False
        except Exception as e:
            print(e)
            invalid = True
    # print(f'Resultado minimos: {lista_coeficientes}')
    xy_print = zip(x_print,y_print)
    if type(lista_coeficientes) != type("string"):
        result_a0 = lista_coeficientes[0]
        result_a1 = lista_coeficientes[1]
        result_a2 = lista_coeficientes[2]
    else:
        result_a0 = lista_coeficientes
        result_a1 = lista_coeficientes
        result_a2 = lista_coeficientes
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "xy_print": xy_print,
        "result_a0": result_a0,
        "result_a1": result_a1,
        "result_a2": result_a2,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_cuadratica.html', context)

@login_required
def preface_cubica(request):
    method = Method.objects.filter(name="Cúbica").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_cubica.html', context)

@login_required
def excercise_cubica(request):
    method = Method.objects.filter(name="Cúbica").first()
    # Variables del problema
    mode = 3
    invalid = True
    while invalid:
        try:
            x,y = random_minimos_cuadrados.generate_minimos_cuadrados()
            x_print = var_value(x)
            y_print = var_value(y)
            lista_coeficientes = minimos_cuadrados_general.metodo_minimos_cuadrados(mode,x,y)
            invalid = False
        except Exception as e:
            print(e)
            invalid = True
    # print(f'Resultado minimos: {lista_coeficientes}')
    xy_print = zip(x_print,y_print)
    if type(lista_coeficientes) != type("string"):
        result_a0 = lista_coeficientes[0]
        result_a1 = lista_coeficientes[1]
        result_a2 = lista_coeficientes[2]
        result_a3 = lista_coeficientes[3]
    else:
        result_a0 = lista_coeficientes
        result_a1 = lista_coeficientes
        result_a2 = lista_coeficientes
        result_a3 = lista_coeficientes
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "xy_print": xy_print,
        "result_a0": result_a0,
        "result_a1": result_a1,
        "result_a2": result_a2,
        "result_a3": result_a3,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_cubica.html', context)

@login_required
def preface_lineal_con_funcion(request):
    method = Method.objects.filter(name="Lineal con función").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_lineal_con_funcion.html', context)

@login_required
def excercise_lineal_con_funcion(request):
    method = Method.objects.filter(name="Lineal con función").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            x,y,funcion = random_minimos_cuadrados_con_funcion.generate_minimos_cuadrados_con_funcion()
            x_print = var_value(x)
            y_print = var_value(y)
            funcion_print = var_value(funcion)
            lista_coeficientes = lineal_con_funcion.metodo_lineal_con_funcion(x,y,funcion)
            invalid = False
        except Exception as e:
            print(e)
            invalid = True
    # print(f'Resultado minimos: {lista_coeficientes}')
    # Variables de presentacion del problema
    funcion_print = parsed_equation(funcion_print)
    xy_print = zip(x_print,y_print)
    if type(lista_coeficientes) != type("string"):
        result_a0 = lista_coeficientes[0]
        result_a1 = lista_coeficientes[1]
        result_a2 = lista_coeficientes[2]
    else:
        result_a0 = lista_coeficientes
        result_a1 = lista_coeficientes
        result_a2 = lista_coeficientes
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "xy_print": xy_print,
        "funcion_print":funcion_print,
        "result_a0": result_a0,
        "result_a1": result_a1,
        "result_a2": result_a2,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_lineal_con_funcion.html', context)

       # # "Minimos Cuadrados"
       # "Linea Recta"
       # "Cuadratica"
       # "Cubica"
