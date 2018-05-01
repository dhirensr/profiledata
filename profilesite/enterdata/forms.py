from django import forms
from .models import EnterData

class NameForm(forms.ModelForm):
    class Meta:
        model=EnterData
        fields=('bachelors_stream','class_10_percent','class_12_percent',\
                'bachelors_percent','work_exp','toefl','gre_score','admit_unis',\
                'reject_unis','ms_stream','extra_curricular','name')

class TestForm(forms.Form,forms.ModelForm):
    class Meta:
        model = EnterData
        fields= ('work_exp','name')
    hint1 = forms.CharField(max_length=30,required=True)
    hint2 = forms.CharField(max_length=30,required=True)
    hint3 = forms.CharField(max_length=30,required=True)
