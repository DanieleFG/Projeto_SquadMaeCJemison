from django.shortcuts import render
from noticias.forms import NoticiasForm
from noticias.models import Noticias, Imagens
from PIL import Image
from django.utils.text import slugify

# Create your views here.

def criar_noticia(request):
    noticia = Noticias.objects.all()
    form = NoticiasForm(request.POST or None, request.FILES or None)
    sucesso = False
    if form.is_valid():
        noticia_obj = form.save(commit=False)
        noticia_obj.save()

        # Salvando a imagem na tabela Imagens
        imagem = request.FILES['imagem']
        extensao = imagem.name.split('.')[-1]
        print(extensao)
        # imagem.name = slugify(imagem.name)
        print(imagem)
        imagem_obj = Imagens(path=imagem, cod_noticia_id=noticia_obj.cod_noticia, extencao=extensao)
        imagem_obj.save()

        sucesso = True
    contexto = {
        'form' : form,
        'sucesso' : sucesso,
        'noticias' : noticia
    }
    return render(request, 'form_noticias.html', contexto)
