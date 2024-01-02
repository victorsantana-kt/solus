from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/<int:id>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('cadastrar/', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    # Adicione mais padrões de URL conforme necessário para suas views
]
