from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Clientes, Tratamento, Exames

class DateInput(forms.DateInput):
    input_type = 'date'

class ClientesModelForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nome',
            'DataNasc',
            'Tel',
            'email',
            'Notas'
        ]
        widgets = {
            'DataNasc': DateInput(),
        }

class TratamentoModelForm(forms.ModelForm):
    class Meta:
        model = Tratamento
        fields = [
            'cliente',
            'datatrat',
            'tipoTrat',
            'Descricao'
        ]
        widgets = {
            'datatrat': DateInput(),
        }

class ExameModelForm(forms.ModelForm):
    class Meta:
        model = Exames
        fields = [
            'cliente',
            'dataex',
            'Descricao',
            'Ficheiro'
        ]
        widgets = {
            'dataex': DateInput(),
        }