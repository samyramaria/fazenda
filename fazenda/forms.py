from django import forms
from .models import Proprietario, Animal

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = ['nome', 'email', 'telefone']


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'idade', 'tipo', 'proprietario']
