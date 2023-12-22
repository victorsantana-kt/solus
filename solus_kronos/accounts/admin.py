from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cliente

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'nome', 'is_active', 'is_staff', 'cliente','filial')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'cliente')
    search_fields = ('username', 'email', 'nome')
    
    

    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('nome', 'cliente', 'filial')}),
    )
    
    
