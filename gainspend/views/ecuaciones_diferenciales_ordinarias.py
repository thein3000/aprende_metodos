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
from gainspend.metodos_numericos import runge_kutta_segundo_orden
from gainspend.metodos_numericos import runge_kutta_tercer_orden
from gainspend.forms import UserMethodForm

@login_required
def preface_runge_kutta_segundo_orden(request):
    method = Method.objects.filter(name="Runge - Kutta (2do orden)").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_runge_kutta_segundo_orden.html', context)

@login_required
def excercise_runge_kutta_segundo_orden(request):
    method = Method.objects.filter(name="Runge - Kutta (2do orden)").first()
    # Variables del problema
    equation = "e**(-t)-3*y"
    y_inicial = 1
    h = .5
    result = runge_kutta_segundo_orden.metodo_runge_kutta_segundo_orden(equation,y_inicial,h)
    # Variables de presentacion del problema
    equation_print = "e**(-t)-3*y"
    y_inicial_print = 1
    h_print = .5
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equation_print": equation_print,
        "y_inicial_print": y_inicial_print,
        "h_print": h_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_runge_kutta_segundo_orden.html', context)

@login_required
def preface_runge_kutta_tercer_orden(request):
    method = Method.objects.filter(name="Runge - Kutta (3er orden)").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_runge_kutta_tercer_orden.html', context)

@login_required
def excercise_runge_kutta_tercer_orden(request):
    method = Method.objects.filter(name="Runge - Kutta (3er orden)").first()
    # Variables del problema
    equation = "(((2*y*t)+1)/y**2)"
    y_inicial = 1
    h = .25
    result = runge_kutta_tercer_orden.metodo_runge_kutta_tercer_orden(equation,y_inicial,h)
    # Variables de presentacion del problema
    equation_print = "(((2*y*t)+1)/y**2)"
    y_inicial_print = 1
    h_print = .25
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equation_print": equation_print,
        "y_inicial_print": y_inicial_print,
        "h_print": h_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_runge_kutta_tercer_orden.html', context)


   # # "Ecuaciones Diferenciales Ordinarias"
   # "Euler hacia adelante"
   # "Euler hacia atras"
   # "Euler modificado"
   # "Runge - Kutta (2do orden)"
   # "Runge - Kutta (3er orden)"
   # "Runge - Kutta (4to orden) por 1/3 de Simpson"
   # "Runge - Kutta (4to orden) por 3/8 de Simpson"
