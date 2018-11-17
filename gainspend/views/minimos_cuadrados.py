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
from gainspend.metodos_numericos import minimos_cuadrados_general
from gainspend.forms import UserMethodForm
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
    x = [ 1.1, 1.9, 2.4, 4.8, 5.1,10.5]
    y = [ 2.5, 2.7, 3.7, 5.2, 6.0, 8.3]
    mode = 1
    lista_coeficientes = minimos_cuadrados_general.metodo_minimos_cuadrados(mode,x,y)
    print(f'Resultado minimos: {lista_coeficientes}')
    # Variables de presentacion del problema
    x_print = [ 1.1, 1.9, 2.4, 4.8, 5.1,10.5]
    y_print = [ 2.5, 2.7, 3.7, 5.2, 6.0, 8.3]
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
       # # "Minimos Cuadrados"
       # "Linea Recta"
       # "Cuadratica"
       # "Cubica"
