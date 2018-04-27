from django import forms
from .models import EnterData

class NameForm(forms.ModelForm):

    class Meta:
        model=EnterData
        fields=('work_exp','german_grade','bachelors_percent')
