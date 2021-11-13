from django import forms
from django.db.models import fields
from .models import Leads


class from_table_model(forms.ModelForm):
    class Meta:
        model = Leads
        fields=('first_name','last_name','age','agent')



class form_table(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


    




 