from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import modulos, permisos, perfil
from django.contrib.auth.decorators import login_required
from .forms import  formPerfil

# Crea tus vista aqui.
@login_required(login_url='/')
def index(request):
    mod = modulos.objects.all().order_by('id')
    user = request.user
    return render_to_response('seguridad/index.html',{'mod':mod,'user':user})

@login_required(login_url='/')
def permisos(request):
    #mod = permisos.objects.all().order_by('id')
    user = request.user
    return render_to_response('seguridad/permisos.html',{'mod':'mod'})

@login_required(login_url='/')
def registrar_perfil(request):
    if request.method == 'GET' and request.is_ajax(): 
        perfiles = perfil.objects.all().order_by('id')

        formu = formPerfil(request.GET)
        if formu.is_valid():
            msm = "perfil guardado"
            formu.save()
        else:
            #msm = "error al guardar"
            formu = formPerfil()

        return render_to_response('seguridad/perfil.html',{'msm':'msm','formu':formu,'perfil':perfiles, 'clase':'perf'})

@login_required(login_url='/')
def elip(request):
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(perfil,pk=idb).delete()
        return HttpResponse('ok')     