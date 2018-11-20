from django.contrib import admin
from .models import Method
from .models import UserMethod

# Register your models here.

admin.site.register(Method)
admin.site.register(UserMethod)
