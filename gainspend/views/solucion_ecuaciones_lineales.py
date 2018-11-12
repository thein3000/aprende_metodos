from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
import datetime
import json
from gainspend.metodos_numericos import montante
from gainspend.forms import UserMethodForm
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
    matriz = [
        [3, 1, 1, 1],
        [1, 4, 1, 2],
        [1, 1, 6, 3]
    ]
    result_x,result_y,result_z = montante.metodo_montante(matriz)
    # Variables de presentacion del problema
    matriz_print = [
        [3, 1, 1, 1],
        [1, 4, 1, 2],
        [1, 1, 6, 3]
    ]
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
    matriz = [
        [3, 1, 1, 1],
        [1, 4, 1, 2],
        [1, 1, 6, 3]
    ]
    result_x,result_y,result_z = montante.metodo_montante(matriz)
    # Variables de presentacion del problema
    matriz_print = [
        [3, 1, 1, 1],
        [1, 4, 1, 2],
        [1, 1, 6, 3]
    ]
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
    matriz = [
        [3, 1, 1, 1],
        [1, 4, 1, 2],
        [1, 1, 6, 3]
    ]
    result_x,result_y,result_z = montante.metodo_montante(matriz)
    # Variables de presentacion del problema
    matriz_print = [
        [3, 1, 1, 1],
        [1, 4, 1, 2],
        [1, 1, 6, 3]
    ]
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


       # # "Solución de Ecuaciones Lineales"
       # "Montante"
       # "Gauss - Jordan"
       # "Eliminación Gaussiana"
       # "Gauss - Seidel"
       # "Jacobi"
