from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ClienteModelForm, ProdutoModelForm
from .models import Produto

# Create your views here.
def index(request):  
    paginas = ['Início', 'História', 'Arcanos Maiores',
              'Arcanos Menores', 'Consulta', 'Contato'] 

    context = {'produtos': Produto.objects.all(),'paginas': paginas }
    return render (request, 'index.html', context)


def contato(request):
    paginas = ['Início', 'História', 'Arcanos Maiores',
              'Arcanos Menores', 'Consulta', 'Contato']
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!!!')
            form = ContatoForm()
        else:
          messages.error(request, 'Erro ao enviar e-mail, tente novamente !!!')
    
    context = {
     'form': form,'paginas': paginas
    }
    return render (request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()           
           messages.success(request,'Produto salvo com sucesso meu filho!!!!')
           form = ProdutoModelForm()
        else:
           messages.error(request, 'Erro ao salvar o produto, tente novamente!!!')
           



    else: form = ProdutoModelForm()
    context = {
        'form': form
    }

           
    return render (request, 'produto.html', context)


def cliente(request):
    formulary = ClienteModelForm(request.POST or None)
    if str(request.method) == 'POST':
        if formulary.is_valid():            
            formulary.save()
            formulary.sendmail()
            messages.success(request, 'Cadastro realizado com sucesso!!!')
            formulary = ClienteModelForm() 
        else:
          messages.error(request, 'Erro no cadastro, tente novamente !!!')    
          formulary = ClienteModelForm()
    context = {
     'form': formulary
    }
    return render (request, 'cliente.html', context)

def historia(request):
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato'] 
    return render (request, 'historia.html',  {'paginas': paginas})

def consulta(request):
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato']
    return render (request, 'consulta.html', {'paginas': paginas})

def maiores(request):
     paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato']
     return render (request, 'maiores.html',  {'paginas': paginas})

def menores(request):
     paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato']
     return render (request, 'menores.html',  {'paginas': paginas})

#ARCANOS  MENORES   
def carta_paus(request, carta): 
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato']
    return render(request, f'{carta}.html',  {'paginas': paginas})

def carta_espadas(request, carta): 
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato'] 
    return render(request, f'{carta}.html',  {'paginas': paginas})

def carta_copas(request, carta):
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato']
    return render(request, f'{carta}.html',  {'paginas': paginas})

def carta_ouros(request, carta):
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores', 'Consulta', 'Contato']
    return render(request, f'{carta}.html',  {'paginas': paginas})



# ARCANOS MAIORES
def arcanos_maiores(request, arcanos): 
    paginas = ['Início','História', 'Arcanos Maiores',
    'Arcanos Menores','Consulta', 'Contato']   
    return render(request, f'{arcanos}.html',  {'paginas': paginas})

