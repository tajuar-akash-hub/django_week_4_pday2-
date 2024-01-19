from django import forms
from musicians.models import musician_Model

class musicians_form(forms.ModelForm):
    class Meta:
        model = musician_Model
        fields = '__all__'