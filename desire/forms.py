from desire.models import Client,VisaAdvisor,customerquerry
from django import forms

class ClientEditProForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username','address', 'dob', 'email','phoneno','password']


class AdviserEditForm(forms.ModelForm):
    class Meta:
        model = VisaAdvisor
        fields=["username","email","phoneno","password","experience","country_specialization","education"]
        

class QueryForm(forms.ModelForm):
    class Meta:
        model = customerquerry
        fields = ['email', 'query', 'adviser']
