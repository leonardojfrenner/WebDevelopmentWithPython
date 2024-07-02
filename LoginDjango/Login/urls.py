"""
URL configuration for Login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from LoginDjango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('', views.LoginDjango, name='home'),
    path('login/', views.fazer_login, name='login'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('login_sucesso/', views.login_sucesso, name='login_sucesso'),
    path('registro_sucesso/', views.registro_sucesso, name='registro_sucesso'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),  
    path('tela_produtos/', views.tela_produtos, name='tela_produtos'),
    path('produto/atualizar/<int:produto_id>/', views.atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:id_produto>',views.excluir_produto,name="excluir_produto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)