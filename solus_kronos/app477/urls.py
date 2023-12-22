from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_bd477, name='list_bd477'),
    # Outras URLs conforme necessário
]