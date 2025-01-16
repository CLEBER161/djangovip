from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.utils import timezone
#from .models import Banco, HistoricoSaldo
from django.contrib import admin
'''
class Socio(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    cpf = models.CharField(max_length=18)
    nome_fantasia= models.CharField(max_length=100)
    inscricao_municipal= models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)
    

    def __str__(self):
        return self.nome


class Favorecido(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    cpf = models.CharField(max_length=18)
    nome_fantasia= models.CharField(max_length=100)
    inscricao_municipal= models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome


class Empresas(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    cpf = models.CharField(max_length=18)
    nome_fantasia= models.CharField(max_length=100)
    inscricao_municipal= models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)

   
    def __str__(self):
        return self.descricao

'''


class CentroCusto(models.Model):
    nome = models.CharField(max_length=255, unique=True)  # Nome único para o centro de custo
    descricao = models.TextField(blank=True, null=True)  # Descrição opcional

    def __str__(self):
        return self.nome
    
    
    
class Banco(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    conta = models.CharField(max_length=20)  
    agencia = models.CharField(max_length=10)  
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    tipodeconta = models.CharField(max_length=50, choices=[('corrente', 'Corrente'), ('poupanca', 'Poupança')], default='corrente')
    conta_pix = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=[('comum', 'Comum'), ('especial', 'Especial')], default='comum')

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Verifica se o saldo foi alterado
        if self.pk:
            banco_antigo = Banco.objects.get(pk=self.pk)
            if banco_antigo.saldo != self.saldo:
                # Cria um histórico de alteração de saldo
                HistoricoSaldo.objects.create(
                    banco=self,
                    saldo_anterior=banco_antigo.saldo,
                    saldo_novo=self.saldo
                )
        super().save(*args, **kwargs)


class HistoricoSaldo(models.Model):
    banco = models.ForeignKey('core.Banco', on_delete=models.CASCADE)  # Referência como string
    saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_novo = models.DecimalField(max_digits=10, decimal_places=2)
    data_alteracao = models.DateTimeField(auto_now_add=True)  # A data é gerada automaticamente

    def __str__(self):
        return f"Histórico {self.banco.nome} - {self.data_alteracao}"
    
class Favorecido(models.Model):
    nome = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    cpf = models.CharField(max_length=18)
    nome_fantasia= models.CharField(max_length=100)
    inscricao_municipal= models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20,
        choices=[('Fornecedor', 'Fornecedor'), ('Socio', 'Socio'),('Funcionario', 'Funcionario')],
        default='Fornecedor'
    )
    def __str__(self):
        return self.nome

class Pagador(models.Model):
    nome = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    cpf = models.CharField(max_length=18)
    nome_fantasia= models.CharField(max_length=100)
    inscricao_municipal= models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemtento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pais= models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    tipodeconta= models.CharField(max_length=50)
    conta_pix=models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20,
        choices=[('Cliente', 'Cliente'), ('Socio', 'Socio')],
        default='Cliente'
    )
    def __str__(self):
        return self.nome



class Pagamento(models.Model):
    descricao = models.CharField(max_length=255)
    favorecido = models.ForeignKey('Favorecido', on_delete=models.CASCADE, related_name='pagamentos')
    observacao = models.TextField(blank=True, null=True)
    banco = models.ForeignKey('Banco', on_delete=models.CASCADE)
    data_prevista = models.DateField()
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    centro_custo = models.ForeignKey('CentroCusto', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('pago', 'Pago')],
        default='pendente'
    )
    responsavel = models.CharField(
        max_length=20,
        choices=[
            ('VIP ADVISER', 'VIP ADVISER'),
            ('VIP ECO', 'VIP ECO'),
            ('VIP EARTH', 'VIP EARTH'),
            ('VIP RETY', 'VIP RETY')
        ],
        default='VIP ADVISER'
    )
    arquivo = models.FileField(upload_to='pagamentos/', blank=True, null=True)

    def __str__(self):
        return self.descricao

    @property
    def categoria(self):
        return self.favorecido.categoria if self.favorecido else 'Sem categoria'

    def save(self, *args, **kwargs):
        # Obtém o status anterior do banco de dados
        if self.pk:
            pagamento_anterior = Pagamento.objects.get(pk=self.pk)
            status_anterior = pagamento_anterior.status
        else:
            status_anterior = None

        # Define a data de pagamento se marcado como 'pago'
        if self.status == 'pago' and not self.data_pagamento:
            self.data_pagamento = timezone.now().date()
        
        # Ajusta o saldo ao mudar para 'pago'
        if self.status == 'pago' and status_anterior != 'pago':
            if self.banco.saldo >= self.valor:
                self.banco.saldo -= self.valor
                self.banco.save()
            else:
                raise ValueError("Saldo insuficiente para realizar o pagamento.")

        # Restaura o saldo ao mudar para 'pendente'
        if status_anterior == 'pago' and self.status == 'pendente':
            self.banco.saldo += self.valor
            self.banco.save()



class Recebimento(models.Model):
    descricao = models.CharField(max_length=255)
    pagador = models.ForeignKey('Pagador', on_delete=models.CASCADE, related_name='recebimentos')
    observacao = models.TextField(blank=True, null=True)
    banco = models.ForeignKey('Banco', on_delete=models.CASCADE)
    data_prevista = models.DateField()
    data_recebimento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    centro_custo = models.ForeignKey('CentroCusto', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('recebido', 'Recebido')],
        default='pendente'
    )
    metodo_pagamento = models.CharField(
        max_length=20,
        choices=[('pix', 'Pix'), ('boleto', 'Boleto') ,('cheque', 'Cheque')],
        default='pix'
    )
    responsavel = models.CharField(
        max_length=20,
        choices=[
            ('VIP ADVISER', 'VIP ADVISER'),
            ('VIP ECO', 'VIP ECO'),
            ('VIP EARTH', 'VIP EARTH'),
            ('VIP RETY', 'VIP RETY')
        ],
        default='VIP ADVISER'
    )
    arquivo = models.FileField(upload_to='recebimentos/', blank=True, null=True)

    def __str__(self):
        return self.descricao

    @property
    def categoria(self):
        return self.favorecido.categoria if self.favorecido else 'Sem categoria'

    def save(self, *args, **kwargs):
        # Obtém o status anterior do banco de dados
        if self.pk:
            recebimento_anterior = Recebimento.objects.get(pk=self.pk)
            status_anterior = recebimento_anterior.status
        else:
            status_anterior = None

        # Define a data de recebimento se marcado como 'recebido'
        if self.status == 'recebido' and not self.data_recebimento:
            self.data_recebimento = timezone.now().date()
        
        # Ajusta o saldo ao mudar para 'recebido'
        if self.status == 'recebido' and status_anterior != 'recebido':
            self.banco.saldo += self.valor
            self.banco.save()

        # Restaura o saldo ao mudar para 'pendente'
        if status_anterior == 'recebido' and self.status == 'pendente':
            self.banco.saldo -= self.valor
            self.banco.save()

        super().save(*args, **kwargs)


class Transferencia(models.Model):
    banco_origem = models.ForeignKey(
        'Banco',
        on_delete=models.CASCADE,
        related_name='transferencias_origem'
    )
    banco_destino = models.ForeignKey(
        'Banco',
        on_delete=models.CASCADE,
        related_name='transferencias_destino'
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_transferencia = models.DateField(default=timezone.now)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    
    responsavel = models.CharField(
        max_length=20,
        choices=[
            ('VIP ADVISER', 'VIP ADVISER'),
            ('VIP ECO', 'VIP ECO'),
            ('VIP EARTH', 'VIP EARTH'),
            ('VIP RETY', 'VIP RETY')
        ],
        default='VIP ADVISER'
    
    )
    
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('transferido', 'Transferido')],
        default='pendente'
    )
    
    arquivo = models.FileField(upload_to='transferencias/', blank=True, null=True)

    def __str__(self):
        return f"Transferência de {self.banco_origem} para {self.banco_destino} - {self.valor}"

    def save(self, *args, **kwargs):
        # Verifica se a origem e destino são diferentes
        if self.banco_origem == self.banco_destino:
            raise ValueError("O banco de origem e destino não podem ser iguais.")

        # Saldo suficiente no banco de origem
        if self.banco_origem.saldo < self.valor:
            raise ValueError("Saldo insuficiente no banco de origem para esta transferência.")

        # Atualiza os saldos
        self.banco_origem.saldo -= self.valor
        self.banco_origem.save()

        self.banco_destino.saldo += self.valor
        self.banco_destino.save()

        super().save(*args, **kwargs)
