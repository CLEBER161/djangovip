from django.urls import path
from django.contrib import admin
from django.urls import path
from core.views import admin
from django.shortcuts import redirect
from .views import index,admin
'''
urlpatterns = [
    path('cadastrar/socio/', views.cadastrar_socio, name='cadastrar_socio'),
    path('listar/socios/', views.socio_list, name='socio_list'),
    path('cadastrar/fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('listar/fornecedores/', views.fornecedor_list, name='fornecedor_list'),
    path('cadastrar/cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar/clientes/', views.cliente_list, name='cliente_list'),
    path('cadastrar/funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('listar/funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('cadastrar/banco/', views.cadastrar_banco, name='cadastrar_banco'),
    path('listar/bancos/', views.banco_list, name='banco_list'),
    path('cadastrar/pagamento/', views.cadastrar_pagamento, name='cadastrar_pagamento'),
    path('listar/pagamentos/', views.pagamento_list, name='pagamento_list'),
]
'''
from core import views

handler500 = views.error500

urlpatterns = [
    path('', lambda request: redirect('/admin/')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
   # path('novo/', novo_pagamento, name='novo_pagamento'),
   # path('editar/<int:pagamento_id>/', editar_pagamento, name='editar_pagamento'),
   # path('deletar/<int:pagamento_id>/', deletar_pagamento, name='deletar_pagamento'),
    
   # path('novo_cliente/', novo_cliente, name='novo_cliente'),
   # path('novo_banco/', novo_banco, name='novo_banco'),
   # path('novo_fornecedor/', novo_fornecedor, name='novo_fornecedor'),
   # path('novo_funcionario/', novo_funcionario, name='novo_funcionario'),
   # path('novo_socio/', novo_socio, name='novo_socio'),
    

   # path('novo_socio', views.novo_socio, name='novo_socio'),
    #path('listar/socios/', views.socio_list, name='socio_list'),
   # path('listar/fornecedor/', views.fornecedor_list, name='fornecedor_list'),
    #path('listar/funcionario/', views.funcionario_list, name='funcionario_list'),
    #path('listar/cliente/', views.cliente_list, name='cliente_list'),
    
   
   
    #path('novo_funcionario/', views.novo_funcionario, name='novo_funcionario'),
]
