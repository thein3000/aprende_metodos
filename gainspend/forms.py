from django import forms
from .models import UserMethod

class UserMethodForm(forms.ModelForm):
    method = forms.IntegerField()
    class Meta:
        model = UserMethod
        fields = ('method','seconds')
