from django.db import models

# Create your models here.
class Noticias(models.Model):
    cod_noticia = models.IntegerField(max_length=20, primary_key=True)
    texto = models.TextField()
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    data = models.DateField(help_text='aaaa-mm-dd')
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
# class Imagens(models.Model):
#     cod_imagem = models.IntegerField(max_length=20, primary_key=True)
#     cod_noticia = models.IntegerField(max_length=20, primary_key=True)
#     path = models.CharField(max_length=50)
#     extencao = models.CharField(max_length=4)
#     create_timestamp = models.DateTimeField(auto_now_add=True)

