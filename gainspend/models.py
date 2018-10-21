# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TableAccounts(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    account = models.TextField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
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
