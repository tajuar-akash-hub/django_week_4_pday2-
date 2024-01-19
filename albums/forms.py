from django import forms 
from albums.models import albums_Model
class album_form(forms.ModelForm):
    class Meta:
        model = albums_Model
        fields = '__all__'
    
