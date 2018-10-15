from django.shortcuts import render
from .models import TableMovements
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required
def main_dashboard(request):
    movements = TableMovements.objects.all()
    context = {
        "movements": movements
    }
    return render(request, 'gainspend/pages/main_dashboard.html', context)

@login_required
def movement_data(request):
    movements = TableMovements.objects.all()
    json = serializers.serialize('json', movements)
    return HttpResponse(json, content_type='application/json')
