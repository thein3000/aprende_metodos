from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.custom_helpers import var_value
from gainspend.metodos_numericos import newton_hacia_adelante
from gainspend.metodos_numericos import newton_hacia_atras
from gainspend.metodos_numericos import lagrange
from gainspend.metodos_numericos import interpolacion_lineal
from gainspend.metodos_numericos import newton_con_diferencias_divididas
from gainspend.randomizers import random_interpolacion
from gainspend.randomizers import random_interpolacion_lineal
# from gainspend.randomizers import

@login_required
def preface_interpolacion_lineal(request):
    method = Method.objects.filter(name="Interpolación lineal").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_interpolacion_lineal.html', context)

@login_required
def excercise_interpolacion_lineal(request):
    method = Method.objects.filter(name="Interpolación lineal").first()
    # Variables del problema
    x,y,t = random_interpolacion_lineal.generate_interpolacion_lineal()
    x_print = var_value(x)
    y_print = var_value(y)
    t_print = var_value(t)
    result = interpolacion_lineal.metodo_interpolacion_lineal(x,y,t)
    # Variables de presentacion del problema
    xy_print = zip(x_print,y_print)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "xy_print": xy_print,
        "t_print": t_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_interpolacion_lineal.html', context)

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
    # Variables del problema
    t,x,y = random_interpolacion.generate_interpolacion(2)
    t_print = var_value(t)
    x_print = var_value(x)
    y_print = var_value(y)
    result = newton_hacia_adelante.metodo_newton_hacia_adelante(t,x,y)
    xy_print = zip(x_print,y_print)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "xy_print": xy_print,
        "t_print": t_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_hacia_adelante.html', context)

@login_required
def preface_newton_hacia_atras(request):
    method = Method.objects.filter(name="Newton hacia atrás").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_hacia_atras.html', context)

@login_required
def excercise_newton_hacia_atras(request):
    method = Method.objects.filter(name="Newton hacia atrás").first()
    # Variables del problema
    t,x,y = random_interpolacion.generate_interpolacion(2)
    t_print = var_value(t)
    x_print = var_value(x)
    y_print = var_value(y)
    result = newton_hacia_adelante.metodo_newton_hacia_adelante(t,x,y)
    xy_print = zip(x_print,y_print)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "xy_print": xy_print,
        "t_print": t_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_hacia_atras.html', context)

@login_required
def preface_lagrange(request):
    method = Method.objects.filter(name="Lagrange").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_lagrange.html', context)

@login_required
def excercise_lagrange(request):
    method = Method.objects.filter(name="Lagrange").first()
    # Variables del problema
    t,x,y = random_interpolacion.generate_interpolacion(1)
    t_print = var_value(t)
    x_print = var_value(x)
    y_print = var_value(y)
    result = newton_hacia_adelante.metodo_newton_hacia_adelante(t,x,y)
    xy_print = zip(x_print,y_print)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "xy_print": xy_print,
        "t_print": t_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_lagrange.html', context)

@login_required
def preface_newton_con_diferencias_divididas(request):
    method = Method.objects.filter(name="Newton con diferencias divididas").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_con_diferencias_divididas.html', context)

@login_required
def excercise_newton_con_diferencias_divididas(request):
    method = Method.objects.filter(name="Newton con diferencias divididas").first()
    # Variables del problema
    t,x,y = random_interpolacion.generate_interpolacion(1)
    t_print = var_value(t)
    x_print = var_value(x)
    y_print = var_value(y)
    result = newton_hacia_adelante.metodo_newton_hacia_adelante(t,x,y)
    xy_print = zip(x_print,y_print)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form":user_method_form,
        "xy_print": xy_print,
        "t_print": t_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_con_diferencias_divididas.html', context)

       # # "Interpolación",
       # "Newton hacia adelante"
       # "Newton hacia atrás"
       # "Newton con diferencias divididas"
       # "Lagrange"
