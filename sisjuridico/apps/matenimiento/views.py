from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.seguridad.models import permisos
from .forms import  formOficina, formAccion
from .models import oficina, accion

# Crea tus vista aqui.
def permi(request,url):
    idp = request.user.idperfil_id
    mod = permisos.objects.filter(idmodulo__url=url, idperfil_id=idp).values('idmodulo__url','buscar','eliminar','editar','insertar','imprimir','ver')
    return mod

@login_required(login_url='/')
def registro_oficina(request):
    oficinas = oficina.objects.all().order_by('id')
    estado =  permi(request, "registro_oficina")
    if request.method == 'POST' and request.is_ajax(): 
        formu = formOficina(request.POST)
        if formu.is_valid():
            formu.save()
        return render(request,'mantenimiento/oficina/ajax_oficina.html',{'oficina':oficinas,'n':'oficinaU','estado':estado})            
    else:
        formu = formOficina()
        return render(request,'mantenimiento/oficina/oficina.html',{'formu':formu,'oficina':oficinas, 'url':'registro_oficina/','n':'oficinaU','estado':estado})

@login_required(login_url='/')
def eliminar_oficina(request):
    oficinas = oficina.objects.all().order_by('id')
    estado =  permi(request, "registro_oficina")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(oficina,pk=idb).delete()
        return render(request,'mantenimiento/oficina/ajax_oficina.html',{'oficina':oficinas,'n':'oficinaU','estado':estado})     

@login_required(login_url='/')
def actualizar_oficina(request):
    oficinas = oficina.objects.all().order_by('id')
    estado =  permi(request, "registro_oficina")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(oficina,pk=idp)
        form=formOficina(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'mantenimiento/oficina/ajax_oficina.html',{'oficina':oficinas,'n':'oficinaU','estado':estado}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(oficina,pk=idp)
        form= formOficina(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_oficina/','n':'oficinaU','u':'oficinaU','estado':estado}) 

@login_required(login_url='/')
def registro_accion(request):
    accions = accion.objects.all().order_by('id')
    estado =  permi(request, "registro_accion")
    if request.method == 'POST' and request.is_ajax(): 
        formu = formAccion(request.POST)
        if formu.is_valid():
            formu.save()
        return render(request,'mantenimiento/accion/ajax_accion.html',{'accion':accions,'n':'accionU','estado':estado})            
    else:
        formu = formAccion()
        return render(request,'mantenimiento/accion/accion.html',{'formu':formu,'accion':accions, 'url':'registro_accion/','n':'accionU','estado':estado})

@login_required(login_url='/')
def eliminar_accion(request):
    accions = accion.objects.all().order_by('id')
    estado =  permi(request, "registro_accion")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(accion,pk=idb).delete()
        return render(request,'mantenimiento/accion/ajax_accion.html',{'accion':accions,'n':'accionU','estado':estado})     

@login_required(login_url='/')
def actualizar_accion(request):
    accions = accion.objects.all().order_by('id')
    estado =  permi(request, "registro_accion")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(accion,pk=idp)
        form=formAccion(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'mantenimiento/accion/ajax_accion.html',{'accion':accions,'n':'accionU','estado':estado}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(accion,pk=idp)
        form= formAccion(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_accion/','n':'accionU','u':'accionU','estado':estado})         