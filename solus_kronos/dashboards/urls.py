from django.urls import path
from .views import criar_dashboard
from .views import listar_dashboards

urlpatterns = [
    path('novo/', criar_dashboard, name='criar_dashboard'),
    path('listar/', listar_dashboards, name='listar_dashboards'),
]
