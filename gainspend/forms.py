from django import forms
from .models import UserMethod

class UserMethodForm(forms.ModelForm):
    method_id = forms.IntegerField()
    class Meta:
        model = UserMethod
        fields = ('method_id','seconds')
