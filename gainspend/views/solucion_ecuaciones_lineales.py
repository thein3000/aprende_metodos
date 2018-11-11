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


       # # "Solución de Ecuaciones Lineales"
       # "Montante"
       # "Gauss - Jordan"
       # "Eliminación Gaussiana"
       # "Gauss - Seidel"
       # "Jacobi"
