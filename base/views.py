from django.shortcuts import render
from base.forms import CadastroUsuarioForm
from base.models import CadastroUsuario

def home(request):
    return render(request, 'home.html')

def cadastroUser(request):
    sucesso = False    
    form = CadastroUsuarioForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastroUsuario.html', contexto)

