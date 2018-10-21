from django.shortcuts import render
from .models import TableMovements
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .forms import MovementsIncomeForm, MovementsExpenseForm
import datetime
import json

@login_required
def main_dashboard(request):
    # Get view data
    movements = TableMovements.objects.all()
    #Prepare and Initialize income and expense forms
    today_date = datetime.date.today()
    time_now = datetime.datetime.now()
    initial_data = { "date":today_date, "time": time_now}
    income_form = MovementsIncomeForm(initial = initial_data)
    expense_form = MovementsExpenseForm(initial = initial_data)
    # Calculate general total, income, and  expense
    total_income = 0
    total_expenses = 0
    current_capital = 0
    for movement in movements:
        if movement.sign == '+':
            total_income = total_income + movement.amount
        else:
            total_expenses = total_expenses + movement.amount

    current_capital = total_income - total_expenses
    context = {
        "movements": movements,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "current_capital": current_capital,
        "income_form": income_form,
        "expense_form": expense_form
    }
    return render(request, 'gainspend/pages/main_dashboard.html', context)

@login_required
def movement_data(request):
    # Data view in json format for ajax access
    movements = TableMovements.objects.all().order_by('-pk')
    json = serializers.serialize('json', movements)
    return HttpResponse(json, content_type='application/json')

@login_required
def register_income(request):
    if request.method == 'POST':
        form = MovementsIncomeForm(request.POST)
        if form.is_valid():
            post_amount = form.cleaned_data['amount']
            post_detail = form.cleaned_data['detail']
            post_date = form.cleaned_data['date']
            post_account = form.cleaned_data['income_account']
            post_category = form.cleaned_data['income_category']
            movement = TableMovements(
                transfer=0,
                amount=post_amount,
                detail=post_detail,
                date=post_date,
                account=post_account,
                category=post_category,
                sign='+')
            movement.save()
            response_data = {}
            response_data['result'] = 'Succesfully registered movement!'
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            response_data = {}
            response_data['result'] = 'Error in validation!'
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@login_required
def register_expense(request):
    if request.method == 'POST':
        form = MovementsExpenseForm(request.POST)
        if form.is_valid(): #form.cleaned_data['subject']
            print(form.cleaned_data)
            post_amount = form.cleaned_data['amount']
            post_detail = form.cleaned_data['detail']
            post_date = form.cleaned_data['date']
            post_account = form.cleaned_data['expense_account']
            post_category = form.cleaned_data['expense_category']
            movement = TableMovements(
                transfer=0,
                amount=post_amount,
                detail=post_detail,
                date=post_date,
                account=post_account,
                category=post_category,
                sign='-')
            movement.save()
            response_data = {}
            response_data['result'] = 'Succesfully registered movement!'
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            print(form.errors)
            response_data = {}
            response_data['result'] = 'Error in validation!'
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
