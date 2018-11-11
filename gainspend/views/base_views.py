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
def main_dashboard(request):
    methods = Method.objects.all()
    context = {
        "methods": methods
    }
    return render(request, 'gainspend/pages/main_dashboard.html', context)

@login_required
def successful_excercise(request):

    context = {
    }
    return render(request, 'gainspend/pages/successful_excercise.html', context)
