from django.shortcuts import render
from .models import Method
from .models import UserMethod
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url
from django.core import serializers
from django.contrib.auth.decorators import login_required
# from .forms import MovementUpdateForm, MovementsIncomeForm, MovementsExpenseForm, MovementsTransferForm
# from .forms import AccountsForm"
# from .forms import CategoriesForm"
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
