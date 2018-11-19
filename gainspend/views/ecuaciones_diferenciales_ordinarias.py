from django.shortcuts import render
from gainspend.models import Method
from gainspend.models import UserMethod
from django.contrib.auth.decorators import login_required
from gainspend.forms import UserMethodForm
from gainspend.custom_helpers import parsed_equation
from gainspend.metodos_numericos import runge_kutta_segundo_orden
from gainspend.metodos_numericos import runge_kutta_tercer_orden
from gainspend.metodos_numericos import runge_kutta_cuarto_orden_por_un_tercio_de_simpson
from gainspend.metodos_numericos import runge_kutta_cuarto_orden_por_tres_octavos_de_simpson
from gainspend.metodos_numericos import euler_modificado
from gainspend.metodos_numericos import euler_hacia_adelante
from gainspend.metodos_numericos import runge_kutta_de_orden_superior

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
    equation_print = parsed_equation(equation)
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
    equation_print = parsed_equation(equation)
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

@login_required
def preface_runge_kutta_cuarto_orden_por_un_tercio_de_simpson(request):
    method = Method.objects.filter(name="Runge - Kutta (4to orden) por 1/3 de Simpson").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_runge_kutta_cuarto_orden_por_un_tercio_de_simpson.html', context)

@login_required
def excercise_runge_kutta_cuarto_orden_por_un_tercio_de_simpson(request):
    method = Method.objects.filter(name="Runge - Kutta (4to orden) por 1/3 de Simpson").first()
    # Variables del problema
    equation = "(y+t)**2/(1-y)"
    y_inicial = .4
    h = .2
    result = runge_kutta_cuarto_orden_por_un_tercio_de_simpson.metodo_runge_kutta_cuarto_orden_por_un_tercio_de_simpson(equation,y_inicial,h)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
    y_inicial_print = .4
    h_print = .2
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
    return render(request, 'gainspend/pages/excercise_runge_kutta_cuarto_orden_por_un_tercio_de_simpson.html', context)

@login_required
def preface_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson(request):
    method = Method.objects.filter(name="Runge - Kutta (4to orden) por 3/8 de Simpson").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson.html', context)

@login_required
def excercise_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson(request):
    method = Method.objects.filter(name="Runge - Kutta (4to orden) por 3/8 de Simpson").first()
    # Variables del problema
    equation = "-y/((y**2)+t)"
    y_inicial = 1
    h = .5
    result = runge_kutta_cuarto_orden_por_tres_octavos_de_simpson.metodo_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson(equation,y_inicial,h)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
    y_inicial_print = 1
    h_print = .5
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
    return render(request, 'gainspend/pages/excercise_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson.html', context)

@login_required
def preface_euler_modificado(request):
    method = Method.objects.filter(name="Euler modificado").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_euler_modificado.html', context)

@login_required
def excercise_euler_modificado(request):
    method = Method.objects.filter(name="Euler modificado").first()
    # Variables del problema
    equation = "sin(t)-(y/2)"
    y_inicial = 1
    h = .5
    y_uno = 1
    result = euler_modificado.metodo_euler_modificado(equation,y_inicial,h,y_uno)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
    y_inicial_print = 1
    h_print = .5
    y_uno_print = 1
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equation_print": equation_print,
        "y_inicial_print": y_inicial_print,
        "y_uno_print": y_uno_print,
        "h_print": h_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_euler_modificado.html', context)

@login_required
def preface_euler_hacia_adelante(request):
    method = Method.objects.filter(name="Euler hacia adelante").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_euler_hacia_adelante.html', context)

@login_required
def excercise_euler_hacia_adelante(request):
    method = Method.objects.filter(name="Euler hacia adelante").first()
    # Variables del problema
    equation = "(5*y*t-1)/3"
    y_inicial = 2
    h = .2
    result = euler_hacia_adelante.metodo_euler_hacia_adelante(equation,y_inicial,h)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
    y_inicial_print = 2
    h_print = .2
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
    return render(request, 'gainspend/pages/excercise_euler_hacia_adelante.html', context)

@login_required
def preface_euler_hacia_atras(request):
    method = Method.objects.filter(name="Euler hacia atras").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_euler_hacia_atras.html', context)

@login_required
def excercise_euler_hacia_atras(request):
    method = Method.objects.filter(name="Euler hacia atras").first()
    # Variables del problema
    equation = "(5*y*t-1)/3"
    y_inicial = 2
    h = .2
    result = euler_hacia_adelante.metodo_euler_hacia_adelante(equation,y_inicial,h)
    # Variables de presentacion del problema
    equation_print = parsed_equation(equation)
    y_inicial_print = 2
    h_print = .2
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
    return render(request, 'gainspend/pages/excercise_euler_hacia_atras.html', context)


@login_required
def preface_runge_kutta_de_orden_superior(request):
    method = Method.objects.filter(name="Runge - Kutta de Orden Superior").first()
    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/preface_runge_kutta_de_orden_superior.html', context)

@login_required
def excercise_runge_kutta_de_orden_superior(request):
    method = Method.objects.filter(name="Runge - Kutta de Orden Superior").first()
    # Variables del problema
    equationt = "2*s*t-y"
    yt = 1.1
    st = 1.2
    ht = .2
    result = runge_kutta_de_orden_superior.metodo_runge_kutta_de_orden_superior(equationt,yt,st,ht)
    # Variables de presentacion del problema
    equationt_print = "y'' = " + parsed_equation(equationt)
    yt_print = 1.1
    st_print = 1.2
    ht_print = .2
    data = {'method_id': method.field_id}
    user_method_form = UserMethodForm(initial=data)
    context = {
        "user_method_form": user_method_form,
        "equationt_print": equationt_print,
        "yt_print": yt_print,
        "st_print": st_print,
        "ht_print": ht_print,
        "result": result,
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_runge_kutta_de_orden_superior.html', context)
   # # "Ecuaciones Diferenciales Ordinarias"
   # "Euler hacia adelante"
   # "Euler hacia atras"
   # "Euler modificado"
   # "Runge - Kutta (2do orden)"
   # "Runge - Kutta (3er orden)"
   # "Runge - Kutta (4to orden) por 1/3 de Simpson"
   # "Runge - Kutta (4to orden) por 3/8 de Simpson"
