from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar', views.cadastrar_nf, name='cadastrar_nf'),
    path('listar', views.listar_nfs, name='listar_nfs'),
    path('teste', views.teste_view, name='teste_view'),
    path('editar/<int:nf_id>/', views.editar_nf, name='editar_nf'),
    path('atualizar-status-ssw/', views.atualizar_status_ssw, name='atualizar_status_ssw'),

]
