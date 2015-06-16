from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.seguridad.models import permisos
from .forms import formCategoria
from .models import categoria

# Crea tus vista aqui.
def permi(request,url):
    idp = request.user.idperfil_id
    mod = permisos.objects.filter(idmodulo__url=url, idperfil_id=idp).values('idmodulo__url','buscar','eliminar','editar','insertar','imprimir','ver')
    return mod

@login_required(login_url='/')
def registro_expediente(request):
    return render_to_response('expediente/registro_expediente.html',{'mod':'mod'})    

@login_required(login_url='/')
def registro_categoria(request):
    categorias = categoria.objects.all().order_by('id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'POST' and request.is_ajax(): 
        formu = formCategoria(request.POST)
        if formu.is_valid():
            formu.save()
        return render(request,'expediente/categoria/ajax_categoria.html',{'categoria':categorias,'n':'categoriaU','estado':estado})            
    else:
        formu = formCategoria()
        return render(request,'expediente/categoria/categoria.html',{'formu':formu,'categoria':categorias, 'url':'registro_categoria/','n':'categoriaU','estado':estado})

@login_required(login_url='/')
def eliminar_categoria(request):
    categorias = categoria.objects.all().order_by('id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(categoria,pk=idb).delete()
        return render(request,'expediente/categoria/ajax_categoria.html',{'categoria':categorias,'n':'categoriaU','estado':estado})     

@login_required(login_url='/')
def actualizar_categoria(request):
    categorias = categoria.objects.all().order_by('id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(categoria,pk=idp)
        form=formCategoria(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'expediente/categoria/ajax_categoria.html',{'categoria':categorias,'n':'categoriaU','estado':estado}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(categoria,pk=idp)
        form= formCategoria(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_categoria/','n':'categoriaU','u':'categoriaU','estado':estado})  
