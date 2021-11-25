from django import forms
from GameZoneApp.models import Game,Customer

class GameForms(forms.ModelForm):
    class Meta:
        model=Game
        fields="__all__"

class CustomerForms(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"