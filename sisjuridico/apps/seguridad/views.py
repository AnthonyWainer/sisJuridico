from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import modulos, permisos, perfil, User
from django.contrib.auth.decorators import login_required
from .forms import  formPerfil, LoginForm, formUsuario, formModulo
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

# Crea tus vista aqui.
def Login(request):
    u = request.user
    if u.is_anonymous():
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

    else:
        return redirect('/sistema')


def LogOut(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def index(request):
    mod = modulos.objects.all()
    return render(request,'seguridad/index.html',{'mod':mod})

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
        return render(request,'seguridad/perfil/ajax_perfil.html',{'perfil':perfiles,'n':'perfilU'})            
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
        if form.is_valid():
            form.save()
            return render(request,'seguridad/perfil/ajax_perfil.html',{'perfil':perfiles,'n':'perfilU'}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(perfil,pk=idp)
        form= formPerfil(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_perfil/','n':'perfilU','u':'perfilU'}) 

@login_required(login_url='/')
def registro_usuario(request):
    usuarios = User.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        formu = formUsuario(request.POST)
        if formu.is_valid():
            formu.save()
        #else:
        return render(request,'seguridad/usuario/ajax_usuario.html',{'usuario':usuarios,'n':'UserU'})            
    else:
        formu = formUsuario()
        return render(request,'seguridad/usuario/usuario.html',{'formu':formu,'usuario':usuarios, 'url':'registro_usuario/','n':'UserU'})

@login_required(login_url='/')
def eliminar_usuario(request):
    usuarios = User.objects.all().order_by('id')
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(User,pk=idb).delete()
        return render(request,'seguridad/usuario/ajax_usuario.html',{'usuario':usuarios,'n':'UserU'})     

@login_required(login_url='/')
def actualizar_usuario(request):
    usuarios = User.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(User,pk=idp)
        form=formUsuario(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'seguridad/usuario/ajax_usuario.html',{'usuario':usuarios,'n':'UserU'}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(User,pk=idp)
        form= formUsuario(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_usuario/','n':'UserU','u':'UserU'}) 

@login_required(login_url='/')
def registro_modulo(request):
    modulo = modulos.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        formu = formModulo(request.POST)
        if formu.is_valid():
            formu.save()
        #else:
        return render(request,'seguridad/modulo/ajax_modulo.html',{'modulo':modulo,'n':'ModuloU'})            
    else:
        formu = formModulo()
        return render(request,'seguridad/modulo/modulo.html',{'formu':formu,'modulo':modulo, 'url':'registro_modulo/','n':'ModuloU','nm':'SubModuloU'})

@login_required(login_url='/')
def eliminar_modulo(request):
    modulo = modulos.objects.all().order_by('id')
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(modulos,pk=idb).delete()
        return render(request,'seguridad/modulo/ajax_modulo.html',{'modulo':modulo,'n':'ModuloU'})     

@login_required(login_url='/')
def actualizar_modulo(request):
    modulo = modulos.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(modulos,pk=idp)
        form=formModulo(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'seguridad/modulo/ajax_modulo.html',{'modulo':modulo,'n':'ModuloU'}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(modulos,pk=idp)
        form= formModulo(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_modulo/','n':'ModuloU'}) 

@login_required(login_url='/')
def eliminar_submodulo(request):
    modulo = modulos.objects.all().order_by('id')
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        
        for i in modulos.objects.filter(pk=idb):
            padre = i.padre 

        get_object_or_404(modulos,pk=idb).delete()
        return render(request,'seguridad/modulo/ajax_submodulo.html',{'modulo':modulo,'nm':'SubModuloU','padre':str(padre)})     

@login_required(login_url='/')
def actualizar_submodulo(request):
    modulo = modulos.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(modulos,pk=idp)
        form=formModulo(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'seguridad/modulo/ajax_submodulo.html',{'modulo':modulo,'nm':'SubModuloU'}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(modulos,pk=idp)
        form= formModulo(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_submodulo/','n':'SubModuloU'}) 

@login_required(login_url='/')
def registro_submodulo(request):

    modulo = modulos.objects.all().order_by('id')
    if request.method == 'POST' and request.is_ajax(): 
        formu = formModulo(request.POST)
        padre = request.POST.get("padre","")
        if formu.is_valid():
            formu.save()
        #else:
        return render(request,'seguridad/modulo/ajax_submodulo.html',{'modulo':modulo,'nm':'SubModuloU','padre':padre}) 
    else:
        idp = request.GET.get("id","")
        modulo = modulos.objects.filter(padre=idp)
        #print(modulo.query) #imprime las consultas en el terminal
        return render(request,'seguridad/modulo/ajax_submodulo.html',{'modulo':modulo,'nm':'SubModuloU','padre':idp}) 
