from django.db import models
from django.contrib.auth.models import User

class TableAccounts(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)

    def account_capital(self):
        movements = TableMovements.objects.filter(account=self.account)
        for movement in movements:
            if movement.sign == '+':
                account_capital = total_income + movement.amount
            else:
                account_capital = total_income - movement.amount

        return account_capital

    class Meta:
        # managed = False
        db_table = 'table_accounts'


class TableCategories(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    category = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_categories'


class TableMovements(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    transfer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_movements'
