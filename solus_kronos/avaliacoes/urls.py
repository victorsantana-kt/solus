from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_formulario_avaliacao, name='exibir_formulario_avaliacao'),
    path('submeter/', views.submeter_avaliacao, name='submeter_avaliacao'),
    path('agradecimento/', views.agradecimento, name='avaliacao_sucesso'),
    # Outras URLs conforme necessário
]
