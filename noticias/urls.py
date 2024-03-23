from django.contrib import admin
from django.urls import path
from noticias.views import criar_noticia
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Noticias'
urlpatterns = [
    path('form_noticias/', criar_noticia, name='form_noticias'),
 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
