
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('lobby.urls')),
    path('clientes/', include('clientes_kronos.urls')),
    path('dashboards/', include('dashboards.urls')),
    path('protocolo_notas_fiscais/', include('protocolo_notas_fiscais.urls')),
    path('477/', include('app477.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('task/', include('task.urls')),
    path('clientes_app/', include('clientes_app.urls')),
    
]

# Configurações para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
