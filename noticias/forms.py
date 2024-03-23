from django import forms 
from noticias.models import Noticias


class NoticiasForm(forms.ModelForm):
    texto = forms.CharField(widget=forms.Textarea)
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # imagem = forms.
    class Meta:
        model = Noticias
        fields = ['cod_noticia', 'titulo', 'texto', 'autor', 'categoria', 'data']

