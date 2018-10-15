# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'


class TableAccounts(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    initial_balance = models.FloatField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    expense = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    negative_max = models.TextField(blank=True, null=True)
    positive_max = models.TextField(blank=True, null=True)
    iso_code = models.TextField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    include_total = models.IntegerField(blank=True, null=True)
    value_type = models.IntegerField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_accounts'


class TableAutomatics(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    each = models.IntegerField(blank=True, null=True)
    repeat = models.IntegerField(blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    initial_date = models.TextField(blank=True, null=True)
    next_date = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_automatics'


class TableBudgets(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    initial_date = models.TextField(blank=True, null=True)
    final_date = models.TextField(blank=True, null=True)
    show = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_budgets'


class TableCardviews(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    id_card = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    show = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_cardviews'


class TableCategories(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_categories'


class TableCurrencies(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    iso_code = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_currencies'


class TableMovements(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    transfer = models.IntegerField(blank=True, null=True)
    date_idx = models.TextField(blank=True, null=True)
    day = models.TextField(blank=True, null=True)
    week = models.TextField(blank=True, null=True)
    fortnight = models.TextField(blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    iso_code = models.TextField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_movements'


class TablePreferences(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_preferences'


class TableRecords(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    title = models.TextField(blank=True, null=True)
    account = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    date_idx = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_records'
