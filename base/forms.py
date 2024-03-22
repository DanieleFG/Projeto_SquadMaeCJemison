from django import forms 
from base.models import CadastroUsuario


class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = CadastroUsuario
        fields = ['nome', 'email', 'senha']
    