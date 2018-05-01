from django import forms
from .models import EnterData

class NameForm(forms.ModelForm):
    class Meta:
        model=EnterData
        fields=('work_exp',)

class TestForm(forms.Form,forms.ModelForm):
    class Meta:
        model = EnterData
        fields= ('work_exp','first_name')
    hint1 = forms.CharField(max_length=30,required=True)
    hint2 = forms.CharField(max_length=30,required=True)
    hint3 = forms.CharField(max_length=30,required=True)
