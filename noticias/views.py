from django.shortcuts import render
from noticias.forms import NoticiasForm
from noticias.models import Noticias

# Create your views here.

def criar_noticia(request):
    noticia = Noticias.objects.all()
    form = NoticiasForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form' : form,
        'sucesso' : sucesso,
        'noticias' : noticia
    }
    return render(request, 'form_noticias.html', contexto)
