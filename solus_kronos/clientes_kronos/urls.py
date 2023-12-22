from django.urls import path
from . import views
from lobby.views import lobby  # Importe a view correta para o lobby

urlpatterns = [
    path('criar/', views.criar_cliente, name='criar_cliente'),
    #path('lobby/', lobby, name='lobby'),
    # Adicione outras URLs para atualizar, listar e deletar clientes conforme necessário
]
