from django.contrib import admin
from .models import Ficticio
from .exporta477 import exporta477

def executar_exporta477(modeladmin, request, queryset):
    exporta477()
    modeladmin.message_user(request, "A função exporta477 foi executada.")

@admin.register(Ficticio)
class FicticioAdmin(admin.ModelAdmin):
    actions = [executar_exporta477]
