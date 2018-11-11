from django.shortcuts import render
from .models import Method
from .models import UserMethod
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
import datetime
import json

@login_required
def main_dashboard(request):
    methods = Method.objects.all()
    context = {
        "methods": methods
    }
    return render(request, 'gainspend/pages/main_dashboard.html', context)


def preface_newton_hacia_adelante(request):
    method = Method.objects.filter(name="Newton hacia adelante").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_hacia_adelante.html', context)

def excercise_newton_hacia_adelante(request):
    method = Method.objects.filter(name="Newton hacia adelante").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_hacia_adelante.html', context)

       # # "Interpolación",
       # "Newton hacia adelante"
       # "Newton hacia atras"
       # "Newton con diferencias divididas"
       # "Lagrange"
       # # "Solución de Ecuaciones no Lineales"
       # "Punto fijo"
       # "Newton - Raphson"
       # "Falsa posición"
       # "Secante"
       # # "Solución de Ecuaciones Lineales"
       # "Montante"
       # "Gauss - Jordan"
       # "Eliminación Gaussiana"
       # "Gauss - Seidel"
       # "Jacobi"
       # # "Minimos Cuadrados"
       # "Linea Recta"
       # "Cuadratica"
       # "Cubica"
       # # "Integración"
       # "Newton - Cotes cerradas"
       # "Newton - Cotes abiertas"
       # "Regla de 1/3 de Simpson"
       # "Regla de 3/8 de Simpson"
       # # "Ecuaciones Diferenciales Ordinarias"
       # "Euler hacia adelante"
       # "Euler hacia atras"
       # "Euler modificado"
       # "Runge - Kutta (2do orden)"
       # "Runge - Kutta (3er orden)"
       # "Runge - Kutta (4to orden) por 1/3 de Simpson"
       # "Runge - Kutta (4to orden) por 3/8 de Simpson"
