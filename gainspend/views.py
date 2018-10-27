from django.shortcuts import render
from .models import TableMovements
from .models import TableAccounts
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .forms import MovementsIncomeForm, MovementsExpenseForm, MovementsTransferForm
from .forms import AccountsForm
from django.shortcuts import get_object_or_404
import datetime
import json

# ------------------------------ ACCOUNT ------------------------------------
@login_required
def account_catalogue(request):
    accounts_form = AccountsForm()
    context = {
        "accounts_form": accounts_form,
        "account": 1
    }
    return render(request, 'gainspend/pages/account_catalogue.html', context)

@login_required
def account_detail(request, field_id):
    # Get view data
    account = TableAccounts.objects.filter(field_id=field_id).first()
    account_description = account.account
    movements = TableMovements.objects.filter(account=account_description)
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
        "account": account,
        "movements": movements,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "current_capital": current_capital,
    }
    return render(request, 'gainspend/pages/account_detail.html', context)

@login_required
def account_data(request):
    # Data view in json format for ajax access
    accounts = TableAccounts.objects.all()
    json = serializers.serialize('json', accounts)
    return HttpResponse(json, content_type='application/json')

@login_required
def account_register(request):
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            post_account = form.cleaned_data['account']
            account = TableAccounts(
                account=post_account
                )
            account.save()
            response_data = {}
            response_data['result'] = 'Succesfully registered account!'
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
def account_delete(request, field_id):
    account = get_object_or_404(TableAccounts, field_id=field_id)
    if request.method == 'POST':
        account.delete()
        response_data = {}
        response_data['result'] = 'Succesfully deleted account!'

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        response_data = {}
        response_data['result'] = 'Error on deletion!'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
 # ------------------------------ CATEGORY ------------------------------------
@login_required
def category_data(request):
    # Data view in json format for ajax access
    categories = TableMovements.objects.all()
    json = serializers.serialize('json', categories)
    return HttpResponse(json, content_type='application/json')

 # ------------------------------ MOVEMENT ------------------------------------
@login_required
def main_dashboard(request):
    # Get view data
    movements = TableMovements.objects.all()
    #Prepare and Initialize income and expense forms
    today_date = datetime.date.today()
    time_now = datetime.datetime.now()
    initial_data = { "date":today_date, "time": time_now}
    initial_date = { "date":today_date}
    income_form = MovementsIncomeForm(initial = initial_data)
    expense_form = MovementsExpenseForm(initial = initial_data)
    transfer_form = MovementsTransferForm(initial = initial_date)
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
        "expense_form": expense_form,
        "transfer_form": transfer_form,
    }
    return render(request, 'gainspend/pages/main_dashboard.html', context)

@login_required
def movement_data(request):
    # Data view in json format for ajax access
    movements = TableMovements.objects.all().order_by('-pk')
    json = serializers.serialize('json', movements)
    return HttpResponse(json, content_type='application/json')

@login_required
def account_movement_data(request, account):
    # Data view in json format for ajax access
    movements = TableMovements.objects.filter(account = account).order_by('-pk')
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

@login_required
def register_transfer(request):
    if request.method == 'POST':
        form = MovementsTransferForm(request.POST)
        if form.is_valid(): #form.cleaned_data['subject']
            print(form.cleaned_data)
            post_amount = form.cleaned_data['amount']
            post_date = form.cleaned_data['date']
            post_account = form.cleaned_data['transfer_account']
            post_receiver = form.cleaned_data['transfer_receiver']
            detail_providing = f'Transfered to {post_receiver}'
            detail_receiving = f'Transfered to {post_account}'
            movement_providing = TableMovements(
                transfer=1,
                amount=post_amount,
                detail= detail_providing,
                date=post_date,
                account=post_account,
                category='Transfer',
                sign='-')
            movement_providing.save()
            movement_receiving = TableMovements(
                transfer=1,
                amount=post_amount,
                detail=detail_receiving,
                date=post_date,
                account=post_receiver,
                category='Transfer',
                sign='+')
            movement_receiving.save()
            response_data = {}
            response_data['result'] = 'Succesfully registered transfer!'
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
