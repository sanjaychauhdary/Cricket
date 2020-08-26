from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
    jersy_number= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required','type':'number'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))

    class Meta:
        model = Player
        fields = ['first_name','last_name','jersy_number','country','image']
    
