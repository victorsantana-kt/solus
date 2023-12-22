from django.shortcuts import render
from .models import Bd477


def list_bd477(request):
    registros = Bd477.objects.all()
    return render(request, 'app477/list.html', {'registros': registros})
