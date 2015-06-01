from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import modulos, permisos, perfil
from django.contrib.auth.decorators import login_required
from .forms import  formPerfil, LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

# Crea tus vista aqui.
def Login(request):
    if request.method == 'POST':
        formulario = LoginForm(request.POST)

        if formulario.is_valid():
            username  = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/sistema')
                else: 
                    msm= "cuenta desactivada"  

        msm = "DATOS INCORRECTOS"
        login = LoginForm()
        return render(request,'seguridad/cuentas/login.html',{'login':login,'msm':msm})
    else:
        login = LoginForm()
        return render(request,'seguridad/cuentas/login.html',{'login':login,'msm':''})        


def LogOut(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def index(request):
    mod = modulos.objects.all().order_by('id')
    user = request.user
    return render(request,'seguridad/index.html',{'mod':mod,'user':user})

@login_required(login_url='/')
def permisos(request):
    #mod = permisos.objects.all().order_by('id')
    user = request.user
    return render(request,'seguridad/permisos.html',{'mod':'mod'})
    
@login_required(login_url='/')
def registrar_perfil(request):
    perfiles = perfil.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        formu = formPerfil(request.POST)
        if formu.is_valid():
            formu.save()
        #else:
        return render(request,'seguridad/perfil/ajax_perfil.html',{'perfil':perfiles})            
    else:
        formu = formPerfil()
        return render(request,'seguridad/perfil/perfil.html',{'formu':formu,'perfil':perfiles, 'url':'registro_perfil/','n':'perfilU'})

@login_required(login_url='/')
def eliminar_perfil(request):
    perfiles = perfil.objects.all().order_by('id')
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(perfil,pk=idb).delete()
        return render(request,'seguridad/perfil/ajax_perfil.html',{'perfil':perfiles,'n':'perfilU'})     

@login_required(login_url='/')
def actualizar_perfil(request):
    perfiles = perfil.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(perfil,pk=idp)
        form=formPerfil(request.POST, instance=a)
        print (form)
        if form.is_valid():
            form.save()
            return render(request,'seguridad/perfil/ajax_perfil.html',{'perfil':perfiles,'n':'perfilU'}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(perfil,pk=idp)
        form= formPerfil(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_perfil/','n':'perfilU'}) 
