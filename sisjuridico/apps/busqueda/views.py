from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from apps.expediente.models import categoria, expedientes, resolucion
from apps.seguridad.models import permisos

import datetime
today  = datetime.datetime.now()
fecha   = today.strftime("%Y-%m-%d") 

# Crea tus vista aqui.
def permi(request,url):
    idp = request.user.idperfil_id
    mod = permisos.objects.filter(idmodulo__url=url, idperfil_id=idp).values('idmodulo__url','buscar','eliminar','editar','insertar','imprimir','ver')
    return mod


@login_required(login_url='/')
def busqueda_especifica(request):
    estado =  permi(request, "busqueda_especifica")
    listaCategoria = [{'id':con.id,'descripcion':con.descripcion} for con in categoria.objects.all()]
    listaResolucion = [{'id':con.id,'numero':con.numero} for con in resolucion.objects.all()]

    if request.method == 'POST': 
        idc = request.POST.get("idc","")
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('id')  
        return render(request,'busqueda/ajax_busqueda_especifica.html',{'lista':expediente,'n':'expedienteU','estado':estado})            
    else:    
        idc= 1
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('id')
        modulo = {'lista':expediente, 'url':'busqueda_especifica/','n':'busquedaU','estado':estado,'idcategoria':listaCategoria, 'idresolucion':listaResolucion,'fecha' :fecha}
        return render(request,  'busqueda/busqueda_especifica.html',modulo )        
