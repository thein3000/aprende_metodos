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
from gainspend.metodos_numericos import regla_tres_octavos_de_simpson
from gainspend.metodos_numericos import regla_un_tercio_de_simpson
from gainspend.forms import UserMethodForm

@login_required
def preface_regla_tres_octavos_de_simpson(request):
    method = Method.objects.filter(name="Regla de 3/8 de Simpson").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_regla_tres_octavos_de_simpson.html', context)

@login_required
def excercise_regla_tres_octavos_de_simpson(request):
    method = Method.objects.filter(name="Regla de 3/8 de Simpson").first()
    # Variables del problema
    integral = "1/(1+x**2)"
    n = 10
    a = 2
    b= 3
    result = regla_tres_octavos_de_simpson.metodo_regla_tres_octavos_de_simpson(integral,a,b,n)
    # Variables de presentacion del problema
    integral_print = "1/(1+x**2)"
    n_print = 10
    a_print = 2
    b_print = 3
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "integral_print": integral_print,
        "n_print": n_print,
        "a_print": a_print,
        "b_print": b_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_regla_tres_octavos_de_simpson.html', context)

@login_required
def preface_regla_un_tercio_de_simpson(request):
    method = Method.objects.filter(name="Regla de 1/3 de Simpson").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_regla_un_tercio_de_simpson.html', context)

@login_required
def excercise_regla_un_tercio_de_simpson(request):
    method = Method.objects.filter(name="Regla de 1/3 de Simpson").first()
    # Variables del problema
    integral = "(cos(x)+x**2)"
    n = 10
    a = 1
    b= 2
    result = regla_un_tercio_de_simpson.metodo_regla_un_tercio_de_simpson(integral,a,b,n)
    # Variables de presentacion del problema
    integral_print = "(cos(x)+x**2)"
    n_print = 3
    a_print = 1
    b_print = 2
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "integral_print": integral_print,
        "n_print": n_print,
        "a_print": a_print,
        "b_print": b_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_regla_un_tercio_de_simpson.html', context)

       # # "Integración"
       # "Newton - Cotes cerradas"
       # "Newton - Cotes abiertas"
       # "Regla de 1/3 de Simpson"
       # "Regla de 3/8 de Simpson"
