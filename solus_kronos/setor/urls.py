from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_setor, name='cadastrar_setor'),
    path('listar/', views.listar_setores, name='listar_setores'),
    # Outras URLs conforme necessário
]
