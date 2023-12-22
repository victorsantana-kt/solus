# lobby/urls.py
from django.urls import path
from .views import lobby,index

urlpatterns = [
    path('', lobby, name='lobby'),
    path('index', index, name='index'),
    
]
