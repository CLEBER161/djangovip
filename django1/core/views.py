from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.urls import path
#from .forms import SocioForm, FornecedorForm, ClienteForm, FuncionarioForm, BancoForm

from .models import Banco,  Pagamento, Favorecido #, Socio,Cliente, Fornecedor, Funcionario,
def index(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'index.html', {'pagamentos': pagamentos})



def error404(request, ex):
    return render(request, '404.html', status=404)

def error500(request):
    return render(request, '500.html', status=500)
'''
# Função para novo novo Sócio
def novo_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socio_list')
    else:
        form = SocioForm()

    return render(request, 'novo_socio.html', {'form': form})



# Função para listar todos os Sócios
def socio_list(request):
    socios = Socio.objects.all()
    return render(request, 'socio_list.html', {'socios': socios})

# Função para novo novo Fornecedor
def novo_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm()

    return render(request, 'novo_fornecedor.html', {'form': form})

# Função para listar todos os Fornecedores
def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor_list.html', {'fornecedores': fornecedores})

# Função para novo novo Cliente
def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()

    return render(request, 'novo_cliente.html', {'form': form})

# Função para listar todos os Clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

# Função para novo novo Funcionario
def novo_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm()

    return render(request, 'novo_funcionario.html', {'form': form})

# Função para listar todos os Funcionarios
def funcionario_list(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})

# Função para novo novo Banco
def novo_banco(request):
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('banco_list')
    else:
        form = BancoForm()

    return render(request, 'novo_banco.html', {'form': form})

# Função para listar todos os Bancos
def banco_list(request):
    bancos = Banco.objects.all()
    return render(request, 'banco_list.html', {'bancos': bancos})

# Função para novo novo Pagamento
def novo_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm()

    return render(request, 'novo_pagamento.html', {'form': form})

# Função para listar todos os Pagamentos
def pagamento_list(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento_list.html', {'pagamentos': pagamentos})





def editar_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)  # Recupera o pagamento pelo ID
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)  # Passa a instância para edição
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')  # Após salvar, redireciona para a lista de pagamentos
    else:
        form = PagamentoForm(instance=pagamento)

    return render(request, 'editar_pagamento.html', {'form': form, 'pagamento': pagamento})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Pagamento

# Função para Deletar Pagamento
def deletar_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':  # A exclusão só acontece após confirmação
        pagamento.delete()
        return redirect('pagamento_list')  # Após deletar, redireciona para a lista de pagamentos

    return render(request, 'deletar_pagamento.html', {'pagamento': pagamento})



from django.shortcuts import render, redirect
from .models import Funcionario

def novo_funcionario(request):
    if request.method == "POST":
        # Captura os dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cnpj = request.POST.get('cnpj')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemtento')
        bairro = request.POST.get('bairro')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        pais = request.POST.get('pais')
        banco = request.POST.get('banco')
        agencia = request.POST.get('agencia')
        conta = request.POST.get('conta')
        tipodeconta = request.POST.get('tipodeconta')
        conta_pix = request.POST.get('conta_pix')

        # Cria um novo objeto no banco de dados
        Funcionario.objects.create(
            nome=nome,
            cpf=cpf,
            cnpj=cnpj,
            cargo=cargo,
            telefone=telefone,
            endereco=endereco,
            numero=numero,
            complemtento=complemento,
            bairro=bairro,
            estado=estado,
            cidade=cidade,
            pais=pais,
            banco=banco,
            agencia=agencia,
            conta=conta,
            tipodeconta=tipodeconta,
            conta_pix=conta_pix
        )

        # Redireciona para uma página de sucesso ou lista de funcionários
        return redirect('funcionario_list')  # Certifique-se de ter essa rota no `urls.py`

    # Se o método for GET, renderiza o formulário vazio
    return render(request, 'novo_funcionario.html')






from django.shortcuts import render

def novo_banco(request):
    return render(request, 'novo_banco.html')

def novo_cliente(request):
    return render(request, 'novo_cliente.html')

def novo_fornecedor(request):
    return render(request, 'novo_fornecedor.html')

def novo_funcionario(request):
    return render(request, 'novo_funcionario.html')

def novo_pagamento(request):
    return render(request, 'novo_pagamento.html')

def novo_socio(request):
    return render(request, 'novo_socio.html')
'''