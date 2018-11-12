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
from gainspend.forms import UserMethodForm


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


   # # "Solución de Ecuaciones no Lineales"
   # "Punto fijo"
   # "Newton - Raphson"
   # "Falsa posición"
   # "Secante"
