from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot as plt
from .models import Venda
import io
import urllib, base64

# Create your views here.

def grafico(request):
    # Obtenha todos os objetos de Venda
    vendas = Venda.objects.all()
    
    # Extraia os meses e quantidades das vendas
    meses = [venda.mes for venda in vendas]
    quantidades = [venda.quantidade for venda in vendas]

    # Crie um gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(meses, quantidades)
    ax.set_xlabel('Meses')
    ax.set_ylabel('Quantidade')
    ax.set_title('Vendas Mensais')

    # Salve o gráfico em um objeto BytesIO
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Converta a imagem para base64 e embede no HTML
    string = base64.b64encode(buf.read()).decode()
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    context = {
        'data':uri
    }

    # Renderize o template com o gráfico embebido
    return render(request,'grafico.html', context)
