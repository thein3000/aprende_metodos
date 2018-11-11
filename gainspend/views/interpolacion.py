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

    context = {
        "method": method
    }
    return render(request, 'gainspend/pages/excercise_newton_hacia_adelante.html', context)
       # # "Interpolación",
       # "Newton hacia adelante"
       # "Newton hacia atras"
       # "Newton con diferencias divididas"
       # "Lagrange"
