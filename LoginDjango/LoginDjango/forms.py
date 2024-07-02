from django import forms
from LoginDjango.models import Usuario
from .models import Produto, Imagem


class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("email", "senha")

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'preco_produto', 'descricao_produto']

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['imagem']