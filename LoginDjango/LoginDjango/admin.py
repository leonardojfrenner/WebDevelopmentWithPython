from django.contrib import admin
from .models import Usuario, Produto,Imagem
# Register your models here.

admin.site.register(Usuario)

admin.site.register(Produto)

admin.site.register(Imagem)