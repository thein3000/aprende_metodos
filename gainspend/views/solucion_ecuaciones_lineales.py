from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from gainspend.custom_helpers import var_value
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.metodos_numericos import montante
from gainspend.randomizers import random_matriz
from gainspend.randomizers import random_jacobi
import numpy as np

@login_required
def preface_montante(request):
    method = Method.objects.filter(name="Montante").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_montante.html', context)

@login_required
def excercise_montante(request):
    method = Method.objects.filter(name="Montante").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            matriz = random_matriz.generate_matriz()
            result_x,result_y,result_z = montante.metodo_montante(matriz)
            invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    matriz_print = var_value(matriz)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "matriz_print": matriz_print,
        "result_x": result_x,
        "result_y": result_y,
        "result_z": result_z,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_montante.html', context)


@login_required
def preface_gauss_jordan(request):
    method = Method.objects.filter(name="Gauss - Jordan").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_gauss_jordan.html', context)

@login_required
def excercise_gauss_jordan(request):
    method = Method.objects.filter(name="Gauss - Jordan").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            matriz = random_matriz.generate_matriz()
            result_x,result_y,result_z = montante.metodo_montante(matriz)
            invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    matriz_print = var_value(matriz)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "matriz_print": matriz_print,
        "result_x": result_x,
        "result_y": result_y,
        "result_z": result_z,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_gauss_jordan.html', context)

@login_required
def preface_eliminacion_gaussiana(request):
    method = Method.objects.filter(name="Eliminación Gaussiana").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_eliminacion_gaussiana.html', context)

@login_required
def excercise_eliminacion_gaussiana(request):
    method = Method.objects.filter(name="Eliminación Gaussiana").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            matriz = random_matriz.generate_matriz()
            result_x,result_y,result_z = montante.metodo_montante(matriz)
            invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    matriz_print = var_value(matriz)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "matriz_print": matriz_print,
        "result_x": result_x,
        "result_y": result_y,
        "result_z": result_z,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_eliminacion_gaussiana.html', context)

@login_required
def preface_jacobi(request):
    method = Method.objects.filter(name="Jacobi").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_jacobi.html', context)

@login_required
def excercise_jacobi(request):
    method = Method.objects.filter(name="Jacobi").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            matriz = random_matriz.generate_matriz()
            jacobi_validation = random_jacobi.generate_jacobi(matriz)
            result_x,result_y,result_z = montante.metodo_montante(matriz)
            invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    matriz_print = var_value(matriz)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "matriz_print": matriz_print,
        "result_x": result_x,
        "result_y": result_y,
        "result_z": result_z,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_jacobi.html', context)

@login_required
def preface_gauss_seidel(request):
    method = Method.objects.filter(name="Gauss - Seidel").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_gauss_seidel.html', context)

@login_required
def excercise_gauss_seidel(request):
    method = Method.objects.filter(name="Gauss - Seidel").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            matriz = random_matriz.generate_matriz()
            gauss_seidel_validation = random_jacobi.generate_jacobi(matriz)
            result_x,result_y,result_z = montante.metodo_montante(matriz)
            invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    matriz_print = var_value(matriz)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "matriz_print": matriz_print,
        "result_x": result_x,
        "result_y": result_y,
        "result_z": result_z,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_gauss_seidel.html', context)


       # # "Solución de Ecuaciones Lineales"
       # "Montante"
       # "Gauss - Jordan"
       # "Eliminación Gaussiana"
       # "Gauss - Seidel"
       # "Jacobi"
