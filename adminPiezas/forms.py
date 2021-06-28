from django import  forms
from django.forms import ModelForm
from .models import Pieza, Residente


class piezaForm(ModelForm):

    class  Meta():
        model = Pieza
        fields = ['id', 'nroPieza', 'estado', 'residente']




