from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import hashlib
from datetime import timedelta
from .models import Usuario
from .models import Produto, Imagem
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm, ImagemForm
import sys

def tela_produtos(request):
    produtos = Produto.objects.all().order_by('-id')  
    return render(request, 'Login_Sucesso.html', {'produtos': produtos})

def ofertas(request):
    produtos = Produto.objects.all().order_by('-id')  
    return render(request, 'ofertas.html', {'produtos': produtos})


def LoginDjango(request):
    return render(request, 'home.html', {'active_slide': 'login'})

def login_sucesso(request):
    nome_usuario = request.GET.get('nome_usuario', 'Usuário')
    produtos = Produto.objects.all()
    return render(request, 'Login_Sucesso.html', {'nome_usuario': nome_usuario, 'produtos': produtos, 'active_slide': 'cadastro'})

def registro_sucesso(request):
    return render(request, 'Cadastro_Sucesso.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está cadastrado. Por favor, use um email diferente.')
            return render(request, 'cadastro.html', {'active_slide': 'registro'})  
        
        if not nome:
            messages.error(request, 'Por favor, insira seu nome.')
            return render(request, 'cadastro.html', {'active_slide': 'registro'}) 
        
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

        novo_usuario = Usuario(nome=nome, senha=senha_criptografada, email=email)
        novo_usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login') 
    return render(request, 'cadastro.html', {'active_slide': 'registro'})

@csrf_exempt
def fazer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

        try:
            usuario = Usuario.objects.get(email=email, senha=senha_criptografada)
        except Usuario.DoesNotExist:
            usuario = None

        if usuario is not None:
            response = redirect('login_sucesso')
            response['Location'] += f'?nome_usuario={usuario.nome}' 
            expire_time = timedelta(seconds=10000)  

            response.set_cookie('email', email, max_age=expire_time.total_seconds())
            response.set_cookie('senha', senha_criptografada, max_age=expire_time.total_seconds())

            return response
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            return render(request, 'home.html', {'active_slide': 'login'})

    return render(request, 'home.html', {'active_slide': 'login'})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        preco_produto = request.POST.get('preco_produto')
        descricao_produto = request.POST.get('descricao_produto')
        imagem_produto = request.FILES.get('imagem_produto')

        if not nome_produto or not preco_produto or not descricao_produto or not imagem_produto:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'Login_Sucesso.html', {'active_slide': 'cadastro'})

        try:
            novo_produto = Produto(nome_produto=nome_produto, preco_produto=preco_produto, descricao_produto=descricao_produto)
            novo_produto.save()
            messages.debug(request, f'Produto {novo_produto.nome_produto} salvo com sucesso.')
            imagem_produto = Image.open(imagem_produto)
            imagem_produto = imagem_produto.convert('RGB')
            imagem_produto = imagem_produto.resize((300, 300))
            draw = ImageDraw.Draw(imagem_produto)
            draw.text((20, 200), f"CONSTRUCT {date.today()}", (255, 255, 255))
            output = BytesIO()
            imagem_produto.save(output, format="JPEG", quality=100)
            output.seek(0)
            img = InMemoryUploadedFile(output, 'ImageField', f'{date.today()}---{novo_produto.id}.jpg', 'image/jpeg', sys.getsizeof(output), None)

            nova_imagem = Imagem(imagem=img, produto=novo_produto)
            nova_imagem.save()
            messages.debug(request, f'Imagem para o produto {novo_produto.nome_produto} salva com sucesso.')

            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('login_sucesso')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao salvar o produto: {e}')
            return render(request, 'Login_Sucesso.html', {'active_slide': 'cadastro'})

    return render(request, 'Login_Sucesso.html', {'active_slide': 'cadastro'})

def atualizar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    imagem_produto = produto.imagem_set.first()
    
    if request.method == 'POST':
        produto_form = ProdutoForm(request.POST, instance=produto)
        imagem_form = ImagemForm(request.POST, request.FILES, instance=imagem_produto)
        
        if produto_form.is_valid() and imagem_form.is_valid():
            produto_form.save()
            imagem = imagem_form.save(commit=False)
            imagem.produto = produto
            imagem.save()
            messages.success(request, f'Produto "{produto.nome_produto}" atualizado com sucesso!')
            return redirect('login_sucesso')
    else:
        produto_form = ProdutoForm(instance=produto)
        imagem_form = ImagemForm(instance=imagem_produto)
    
    return render(request, 'atualizar_produto.html', {'produto_form': produto_form, 'imagem_form': imagem_form})

def excluir_produto(request,id_produto):
    produto = Produto.objects.get(id=id_produto)
    produto.delete()
    return redirect('login_sucesso')
