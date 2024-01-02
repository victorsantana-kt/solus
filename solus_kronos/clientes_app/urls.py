# clientes_app/urls.py

from django.urls import path
from .views import cadastrar_cliente, lista_clientes

urlpatterns = [
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar/', lista_clientes, name='lista_clientes'),
    # ... outras urls ...
]
