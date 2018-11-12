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
from gainspend.metodos_numericos import newton_hacia_adelante
from gainspend.metodos_numericos import newton_hacia_atras
from gainspend.metodos_numericos import metodo_lagrange
from gainspend.forms import UserMethodForm

@login_required
def preface_newton_hacia_adelante(request):
    method = Method.objects.filter(name="Newton hacia adelante").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_hacia_adelante.html', context)

@login_required
def excercise_newton_hacia_adelante(request):
    method = Method.objects.filter(name="Newton hacia adelante").first()
    t = 3.5
    x = [1,2,3,4]
    y = [120,94,75,62]
    result = newton_hacia_adelante.metodo_newton_hacia_adelante(t,x,y)
    t_print = 3.5
    x_print = [1,2,3,4]
    y_print = [120,94,75,62]
    xy_print = zip(x_print,y_print)
    user_method_form = UserMethodForm()
    context = {
        "user_method_form":user_method_form,
        "xy_print": xy_print,
        "t_print": t_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_hacia_adelante.html', context)



       # # "Interpolación",
       # "Newton hacia adelante"
       # "Newton hacia atras"
       # "Newton con diferencias divididas"
       # "Lagrange"
