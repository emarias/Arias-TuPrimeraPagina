from django import forms 

class FormularioCreacionParticipante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()