from django.db import models
from django.contrib.auth.models import User

class Method(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)
    name = models.TextField(blank=True, null=True)
    is_subject = models.BooleanField(blank=True, null=True)
    preface_name = models.TextField(blank=True, null=True)

class UserMethod(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE)
    method = models.ForeignKey(Method, null=True, blank=True, on_delete = models.CASCADE)
    seconds = models.IntegerField(blank=True, null=True)
