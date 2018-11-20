from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.custom_helpers import var_value
from gainspend.custom_helpers import parsed_equation
from gainspend.metodos_numericos import newton_raphson
from gainspend.metodos_numericos import punto_fijo
from gainspend.metodos_numericos import falsa_posicion
from gainspend.metodos_numericos import secante
from gainspend.randomizers import random_ecuacion_no_lineal

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
    invalid = True
    while invalid:
        try:
            equation = random_ecuacion_no_lineal.generate_ecuacion_no_lineal()
            result = newton_raphson.metodo_newton_raphson(equation)
            if result == 1 or abs(result) < 0.0001 or result == 0:
                invalid = True
            else:
                invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
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
    # invalid = True
    # while invalid:
    #     try:
    #         equation = random_ecuacion_no_lineal.generate_ecuacion_no_lineal()
    #         result = punto_fijo.metodo_punto_fijo(equation)
    #         if result == 1 or abs(result) < 0.0001 or result == 0:
    #             invalid = True
    #         else:
    #             invalid = False
    #     except Exception as e:
    #         print(e)
    #         invalid = True
    result = punto_fijo.metodo_punto_fijo(equation)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
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
    equation_print = parsed_equation(equation)
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

@login_required
def preface_secante(request):
    method = Method.objects.filter(name="Secante").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_secante.html', context)

@login_required
def excercise_secante(request):
    method = Method.objects.filter(name="Secante").first()
    # Variables del problema
    equation="e**(-x) - x"
    result = secante.metodo_secante(equation)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
    # Datos del formulario
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equation_print": equation_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_secante.html', context)


   # # "Solución de Ecuaciones no Lineales"
   # "Punto fijo"
   # "Newton - Raphson"
   # "Falsa posición"
   # "Secante"
