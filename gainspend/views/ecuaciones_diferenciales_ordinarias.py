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


   # # "Ecuaciones Diferenciales Ordinarias"
   # "Euler hacia adelante"
   # "Euler hacia atras"
   # "Euler modificado"
   # "Runge - Kutta (2do orden)"
   # "Runge - Kutta (3er orden)"
   # "Runge - Kutta (4to orden) por 1/3 de Simpson"
   # "Runge - Kutta (4to orden) por 3/8 de Simpson"
