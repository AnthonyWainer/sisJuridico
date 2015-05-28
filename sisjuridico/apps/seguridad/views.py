from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from apps.seguridad.models import modulos
from django.contrib.auth.decorators import login_required

# Crea tus vista aqui.
@login_required(login_url='/')
def index(request):
    mod = modulos.objects.all().order_by('id')
    user = request.user
    return render_to_response('seguridad/index.html',{'mod':mod,'user':user})

@login_required(login_url='/')
def registro_expediente(request):
    return render_to_response('seguridad/registro_expediente.html',{'mod':'mod'})    


