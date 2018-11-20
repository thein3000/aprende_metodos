from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.custom_helpers import parsed_equation, var_value
from gainspend.metodos_numericos import regla_tres_octavos_de_simpson
from gainspend.metodos_numericos import regla_un_tercio_de_simpson
from gainspend.metodos_numericos import newton_cotes_abiertas
from gainspend.metodos_numericos import newton_cotes_cerradas
from gainspend.metodos_numericos import regla_trapezoidal
from gainspend.randomizers import random_integral

@login_required
def preface_regla_trapezoidal(request):
    method = Method.objects.filter(name="Regla Trapezoidal").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_regla_trapezoidal.html', context)

@login_required
def excercise_regla_trapezoidal(request):
    method = Method.objects.filter(name="Regla Trapezoidal").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            integral,a,b,n = random_integral.generate_integral(1)
            integral_print = var_value(integral)
            n_print = var_value(n)
            a_print = var_value(a)
            b_print = var_value(b)
            result = regla_trapezoidal.metodo_regla_trapezoidal(integral,n,a,b)
            if result == 1 or abs(result) < 0.0001 or result == 0:
                invalid = True
            else:
                invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    integral_print = parsed_equation(f'({integral_print}) dx')
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
    return render(request, 'gainspend/pages/excercise_regla_trapezoidal.html', context)

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
    invalid = True
    while invalid:
        try:
            integral,a,b,n = random_integral.generate_integral(1)
            integral_print = var_value(integral)
            n_print = var_value(n)
            a_print = var_value(a)
            b_print = var_value(b)
            result = regla_tres_octavos_de_simpson.metodo_regla_tres_octavos_de_simpson(integral,a,b,n)
            if result == 1 or abs(result) < 0.0001 or result == 0:
                invalid = True
            else:
                invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    integral_print = parsed_equation(f'({integral}) dx')
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
    invalid = True
    while invalid:
        try:
            integral,a,b,n = random_integral.generate_integral(1)
            integral_print = var_value(integral)
            n_print = var_value(n)
            a_print = var_value(a)
            b_print = var_value(b)
            result = regla_un_tercio_de_simpson.metodo_regla_un_tercio_de_simpson(integral,a,b,n)
            if result == 1 or abs(result) < 0.0001 or result == 0:
                invalid = True
            else:
                invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    integral_print = parsed_equation(f'({integral}) dx')
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

@login_required
def preface_newton_cotes_abiertas(request):
    method = Method.objects.filter(name="Newton - Cotes abiertas").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_cotes_abiertas.html', context)

@login_required
def excercise_newton_cotes_abiertas(request):
    method = Method.objects.filter(name="Newton - Cotes abiertas").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            integral,a,b,n = random_integral.generate_integral(1)
            integral_print = var_value(integral)
            n_print = var_value(n)
            a_print = var_value(a)
            b_print = var_value(b)
            result = newton_cotes_abiertas.metodo_newton_cotes_abiertas(integral,a,b,n)
            if result == 1 or abs(result) < 0.0001 or result == 0:
                invalid = True
            else:
                invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    integral_print = parsed_equation(f'({integral}) dx')
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
    return render(request, 'gainspend/pages/excercise_newton_cotes_abiertas.html', context)

@login_required
def preface_newton_cotes_cerradas(request):
    method = Method.objects.filter(name="Newton - Cotes cerradas").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_newton_cotes_cerradas.html', context)

@login_required
def excercise_newton_cotes_cerradas(request):
    method = Method.objects.filter(name="Newton - Cotes cerradas").first()
    # Variables del problema
    invalid = True
    while invalid:
        try:
            integral,a,b,n = random_integral.generate_integral(1)
            integral_print = var_value(integral)
            n_print = var_value(n)
            a_print = var_value(a)
            b_print = var_value(b)
            result = newton_cotes_cerradas.metodo_newton_cotes_cerradas(integral,a,b,n)
            if result == 1 or abs(result) < 0.0001 or result == 0:
                invalid = True
            else:
                invalid = False
        except Exception as e:
            invalid = True
    # Variables de presentacion del problema
    integral_print = parsed_equation(f'({integral}) dx')
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
    return render(request, 'gainspend/pages/excercise_newton_cotes_cerradas.html', context)

       # # "Integración"
       # "Newton - Cotes cerradas"
       # "Newton - Cotes abiertas"
       # "Regla de 1/3 de Simpson"
       # "Regla de 3/8 de Simpson"
