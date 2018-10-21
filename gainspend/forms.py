from django import forms
from .models import TableMovements
from .models import TableAccounts
from .models import TableCategories


class MovementsIncomeForm(forms.ModelForm):
    accounts_list = list(TableAccounts.objects.values_list('account','account'))
    categories_list = list(TableCategories.objects.values_list('category','category'))
    income_account = forms.ChoiceField(choices=accounts_list)
    income_category = forms.ChoiceField(choices=categories_list)
    class Meta:
        model = TableMovements
        fields  = ['amount','detail','date','income_account','income_category']
        widgets = {
            'amount': forms.NumberInput(attrs={'id':'id_income_amount'}),
            'detail': forms.TextInput(attrs={'id':'id_income_detail'}),
            'date': forms.DateInput(attrs={'id':'id_income_date'})
        }

class MovementsExpenseForm(forms.ModelForm):
    accounts_list = list(TableAccounts.objects.values_list('account','account'))
    categories_list = list(TableCategories.objects.values_list('category','category'))
    expense_account = forms.ChoiceField(choices=accounts_list)
    expense_category = forms.ChoiceField(choices=categories_list)
    class Meta:
        model = TableMovements
        fields  = ['amount','detail','date','expense_account','expense_category']
        widgets = {
            'amount': forms.NumberInput(attrs={'id':'id_expense_amount'}),
            'detail': forms.TextInput(attrs={'id':'id_expense_detail'}),
            'date': forms.DateInput(attrs={'id':'id_expense_date'})
        }
