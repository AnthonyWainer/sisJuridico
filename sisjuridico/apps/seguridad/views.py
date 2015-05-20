from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from apps.seguridad.models import modulos

# Crea tus vista aqui.
def index(request):
    mod = modulos.objects.all().order_by('id')
    return render_to_response('seguridad/index.html',{'mod':mod})

