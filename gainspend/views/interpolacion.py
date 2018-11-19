from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.metodos_numericos import newton_hacia_adelante
from gainspend.metodos_numericos import newton_hacia_atras
from gainspend.metodos_numericos import lagrange
from gainspend.metodos_numericos import interpolacion_lineal
from gainspend.metodos_numericos import newton_con_diferencias_divididas
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
    t = 3
    x = [2,4]
    y = [.69314718,1.386294361]
    result = interpolacion_lineal.metodo_interpolacion_lineal(x,y,t)
    # Variables de presentacion del problema
    t_print = 3
    x_print = [2,4]
    y_print = [.69314718,1.386294361]
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
    t = 3.5
    x = [1,2,3,4]
    y = [120,94,75,62]
    result = newton_hacia_adelante.metodo_newton_hacia_adelante(t,x,y)
    # Variables de presentacion del problema
    t_print = 3.5
    x_print = [1,2,3,4]
    y_print = [120,94,75,62]
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
    method = Method.objects.filter(name="Newton hacia atras").first()

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_hacia_atras.html', context)

@login_required
def excercise_newton_hacia_atras(request):
    method = Method.objects.filter(name="Newton hacia atras").first()
    # Variables del problema
    t = 3.5
    x = [1,2,3,4]
    y = [120,94,75,62]
    result = newton_hacia_atras.metodo_newton_hacia_atras(t,x,y)
    # Variables de presentacion del problema
    t_print = 3.5
    x_print = [1,2,3,4]
    y_print = [120,94,75,62]
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
    t = 3.5
    x = [1,2,3,4]
    y = [120,94,75,62]
    result = lagrange.metodo_lagrange(t,x,y)
    # Variables de presentacion del problema
    t_print = 3.5
    x_print = [1,2,3,4]
    y_print = [120,94,75,62]
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
    t = 7
    x = [7.3,6.5,6.1,5.5]
    y = [-.28,-1.35,-1.96,-2.74]
    result = newton_con_diferencias_divididas.metodo_newton_con_diferencias_divididas(x,y,t)
    # Variables de presentacion del problema
    t_print = 7
    x_print = [7.3,6.5,6.1,5.5]
    y_print = [-.28,-1.35,-1.96,-2.74]
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
       # "Newton hacia atras"
       # "Newton con diferencias divididas"
       # "Lagrange"
