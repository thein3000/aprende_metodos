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
from gainspend.metodos_numericos import newton_raphson
from gainspend.metodos_numericos import punto_fijo
from gainspend.metodos_numericos import falsa_posicion
from gainspend.forms import UserMethodForm
from sympy import pretty, symbols, pprint


@login_required
def preface_newton_raphson(request):
    method = Method.objects.filter(name="Newton - Raphson").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_raphson.html', context)

@login_required
def excercise_newton_raphson(request):
    method = Method.objects.filter(name="Newton - Raphson").first()
    # Variables del problema
    equation = "0.8*x**2 + x - 3"
    result = newton_raphson.metodo_newton_raphson(equation)
    # Variables de presentacion del problema
    equation_print = "0.8*x**2 + x - 3"
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "equation_print": equation_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_raphson.html', context)

@login_required
def preface_punto_fijo(request):
    method = Method.objects.filter(name="Punto fijo").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_punto_fijo.html', context)

@login_required
def excercise_punto_fijo(request):
    method = Method.objects.filter(name="Punto fijo").first()
    # Variables del problema
    equation = "(e**x - 2) / 2"
    result = punto_fijo.metodo_punto_fijo(equation)
    # Variables de presentacion del problema
    equation_print = "(e**x - 2) / 2"
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equation_print": equation_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_punto_fijo.html', context)

@login_required
def preface_falsa_posicion(request):
    method = Method.objects.filter(name="Falsa posición").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_falsa_posicion.html', context)

@login_required
def excercise_falsa_posicion(request):
    method = Method.objects.filter(name="Falsa posición").first()
    # Variables del problema
    equation = "x*e**x - 10"
    result = falsa_posicion.metodo_falsa_posicion(equation)
    # Variables de presentacion del problema
    equation_print = "x*e**x - 10"
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equation_print": equation_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_falsa_posicion.html', context)


   # # "Solución de Ecuaciones no Lineales"
   # "Punto fijo"
   # "Newton - Raphson"
   # "Falsa posición"
   # "Secante"
