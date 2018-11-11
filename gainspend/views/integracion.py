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


       # # "Integración"
       # "Newton - Cotes cerradas"
       # "Newton - Cotes abiertas"
       # "Regla de 1/3 de Simpson"
       # "Regla de 3/8 de Simpson"
