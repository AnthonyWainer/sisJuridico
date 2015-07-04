from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from apps.seguridad.models import permisos
from apps.reportes.models import historial
from .forms import formCategoria, formExpediente, formHojadeEnvio, formResolucion, formExpedienteA, formHojadeEnvioU,formResolucionA
from .models import categoria, expedientes, hojaEnvio, accion, oficina, resolucion
from apps.paginacion import paginacion
import datetime, time
today  = datetime.datetime.now()
fecha  = today.strftime("%Y-%m-%d")
hora   = time.strftime("%H:%M:%S") 

# Crea tus vista aqui.
def historiales(request,mod):
    ip        = request.META['REMOTE_ADDR']
    equipo    = request.META['HTTP_USER_AGENT']
    a = historial()
    a.idusuario_id  = request.user.id
    a.fecha         = fecha
    a.hora          = hora
    a.equipo        = equipo
    a.ip            = ip 
    a.modulo        = mod[0]
    a.accion        = mod[1]
    a.idaccion      = mod[2]
    a.save()


def permi(request,url):
    idp = request.user.idperfil_id
    mod = permisos.objects.filter(idmodulo__url=url, idperfil_id=idp).values('idmodulo__url','buscar','eliminar','editar','insertar','imprimir','ver')
    return mod

@login_required(login_url='/')
def registro_expediente(request):
    estado =  permi(request, "registro_expediente")
    listaCategoria = [{'id':con.id,'descripcion':con.descripcion} for con in categoria.objects.all()]
    listaResolucion = [{'id':con.id,'numero':con.numero} for con in resolucion.objects.all()]

    #print(request.POST)
    if request.method == 'POST': 
        idd = request.POST.get("id","")
        if idd == "undefined":
            idc = 1
            formu = formExpediente(request.POST,request.FILES )
            if formu.is_valid():
                formu.save()
                idp = expedientes.objects.latest('id')
                historiales(request,["expediente","registrar",idp.id])
            else:
                return render(request,'expediente/expediente/form_exp.html',{'formu':formu})
        else:
            idc = request.POST.get("idc","")
        
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('-id')  
        return render(request,'expediente/expediente/ajax_expediente.html',{'lista':expediente,'n':'expedienteU','estado':estado})            
    else:
        idc= 1
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('-id')
        formu = formExpediente()
        modulo = {'formu':formu, 'url':'registro_expediente/','n':'expedienteU','estado':estado,'idcategoria':listaCategoria, 'idresolucion':listaResolucion}
        return paginacion(request,expediente, modulo, 'expediente/expediente/expediente.html' )        

@login_required(login_url='/')
def actualizar_expediente(request):
    expediente = expedientes.objects.all().order_by('-id')
    estado =  permi(request, "registro_expediente")
    if request.method == 'POST': 
        idp = request.POST.get("id","")
        a=get_object_or_404(expedientes,pk=idp)
        form=formExpedienteA(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()       
            historiales(request,["expediente","actualizar",idp])
            return render(request,'expediente/expediente/ajax_expediente.html',{'lista':expediente,'n':'expedienteU','estado':estado}) 
        else:
            return render(request,'expediente/expediente/form_exp.html',{'formu':form})             
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(expedientes,pk=idp)
        form= formExpedienteA(instance=a)
        return render(request,'expediente/expediente/modal.html',{'formu':form,'url':'actualizar_expediente/','n':'expedienteU','u':'expedienteU','estado':estado})  


@login_required(login_url='/')
def eliminar_expediente(request):
    expediente = expedientes.objects.all().order_by('-id')
    estado =  permi(request, "registro_expediente")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(expedientes,pk=idb).delete()
        historiales(request,["expediente","eliminar",idb])
        return render(request,'expediente/expediente/ajax_expediente.html',{'lista':expediente,'n':'expedienteU','estado':estado})     

def busq_ajax_exp(request):
    dat = request.GET.get('datos')
    estado =  permi(request, "registro_expediente")
    e = expedientes.objects.filter( Q(nro__contains=dat))[:10]
    modulo = {'lista':e,'n':'expedienteU','estado':estado}
    return render(request,'expediente/expediente/ajax_expediente.html', modulo)

@login_required(login_url='/')
def registro_hoja_envio(request):
    
    estado =  permi(request, "registro_hoja_envio")
    listaAccion = [{'id':con.id,'accion':con.accion} for con in accion.objects.all()]
    listaOficina = [{'id':con.id,'oficina':con.oficina} for con in oficina.objects.all()]
    listaExpediente = [{'id':con.id,'nro': con.nro} for con in expedientes.objects.all()]

    if request.method == 'POST': 
        idd = request.POST.get("id","")
        if idd == "undefined":
            idc = 1
            formH = formHojadeEnvio(request.POST,request.FILES )
            if formH.is_valid():
                formH.save()
                idp = hojaEnvio.objects.latest('id')                                
                historiales(request,["hojaEnvio","registrar",idp.id])
            else:
                return render(request,'expediente/hoja_envio/form_hoj.html',{'formuH':formH})                
        else:
            idc = request.POST.get("idc","")  
        
        hojaEnvios = hojaEnvio.objects.values('id','idaccion__accion','idoficina__oficina','asunto','observaciones','fecha_emision','fecha_recepcion','documento_adjun','num_follos').filter(idexpediente=idc).order_by('id')            
        return render(request,'expediente/hoja_envio/ajax_hoja_envio.html',{'hoja_envio':hojaEnvios,'n':'hoja_envioU','estado':estado})            
    else:
        idc = 1
        hojaEnvios = hojaEnvio.objects.values('id','idaccion__accion','idoficina__oficina','asunto','observaciones','fecha_emision','fecha_recepcion','documento_adjun','num_follos').filter(idexpediente=idc).order_by('id')            
        formH = formHojadeEnvio()
        modulo = {'formuH':formH,'url':'registro_hoja_envio/','n':'hoja_envioU','estado':estado,'idaccion':listaAccion,'idoficina':listaOficina,'idexpediente':listaExpediente}
        return paginacion(request,hojaEnvios, modulo, 'expediente/hoja_envio/hoja_envio.html' )        

@login_required(login_url='/')
def actualizar_hoja_envio(request):
    hojaEnvios = hojaEnvio.objects.values('id','idaccion__accion','idoficina__oficina','asunto','observaciones','fecha_emision','fecha_recepcion','documento_adjun','num_follos').order_by('id')
    estado =  permi(request, "registro_hoja_envio")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(hojaEnvio,pk=idp)
        form=formHojadeEnvioU(request.POST, instance=a)
        if form.is_valid():
            form.save()
            historiales(request,["hojaEnvio","actualizar",idp])
            return render(request,'expediente/hoja_envio/ajax_hoja_envio.html',{'hoja_envio':hojaEnvios,'n':'hoja_envioU','estado':estado})            
        else:
            return render(request,'expediente/hoja_envio/form_hoj.html',{'formuH':form})            
        
        
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(hojaEnvio,pk=idp)
        form= formHojadeEnvioU(instance=a)
        return render(request,'expediente/hoja_envio/modal.html',{'formuH':form,'url':'actualizar_hoja_envio/','n':'hoja_envioU','u':'hoja_envioU','estado':estado})  

@login_required(login_url='/')
def eliminar_hoja_envio(request):
    hojaEnvios = hojaEnvio.objects.all().order_by('id')
    estado =  permi(request, "registro_hoja_envio")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(hojaEnvio,pk=idb).delete()
        historiales(request,["hojaEnvio","eliminar",idb])
        return render(request,'expediente/hoja_envio/ajax_hoja_envio.html',{'hoja_envio':hojaEnvios,'n':'hoja_envioU','estado':estado})     



@login_required(login_url='/')
def registro_resolucion(request):

    resoluciones = resolucion.objects.all().order_by('-id')
    estado =  permi(request, "registro_resolucion")

    if request.method == 'POST': 
        formH = formResolucion(request.POST,request.FILES )
        #print (formH)
        if formH.is_valid():
            formH.save()
            idp = resolucion.objects.latest('id')
            historiales(request,["resolucion","registrar",idp.id])
            return render(request,'expediente/resolucion/ajax_resolucion.html',{'lista':resoluciones,'n':'resolucionU','estado':estado})            
        else:
            return render(request,'expediente/resolucion/form_re.html',{'formuH':formH})                        
        
    else:
        formH = formResolucion()
        modulo = {'formuH':formH,'url':'registro_resolucion/','n':'resolucionU','estado':estado}
        return paginacion(request,resoluciones, modulo, 'expediente/resolucion/resolucion.html' )

@login_required(login_url='/')
def actualizar_resolucion(request):
    resoluciones = resolucion.objects.all().order_by('-id')
    estado =  permi(request, "registro_resolucion")
    if request.method == 'POST': 
        idp = request.POST.get("id","")
        a=get_object_or_404(resolucion,pk=idp)
        form=formResolucionA(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            historiales(request,["resolucion","actualizar",idp])
            return render(request,'expediente/resolucion/ajax_resolucion.html',{'lista':resoluciones,'n':'resolucionU','estado':estado}) 
        else:
            return render(request,'expediente/resolucion/form_re.html',{'formuH':form})              
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(resolucion,pk=idp)
        form= formResolucionA(instance=a)
        return render(request,'expediente/resolucion/modal.html',{'formuH':form,'url':'actualizar_resolucion/','n':'resolucionU','u':'resolucionU','estado':estado})  


@login_required(login_url='/')
def eliminar_resolucion(request):
    resoluciones = resolucion.objects.all().order_by('-id')
    estado =  permi(request, "registro_resolucion")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(resolucion,pk=idb).delete()
        historiales(request,["resolucion","eliminar",idb])
        return render(request,'expediente/resolucion/ajax_resolucion.html',{'lista':resoluciones,'n':'resolucionU','estado':estado})     


def busq_ajax_re(request):
    dat = request.GET.get('datos')
    estado =  permi(request, "registro_resolucion")
    e = resolucion.objects.filter( Q(numero__contains=dat))[:10]
    modulo = {'lista':e,'n':'resolucionU','estado':estado}
    return render(request,'expediente/resolucion/ajax_resolucion.html', modulo)


@login_required(login_url='/')
def registro_categoria(request):
    categorias = categoria.objects.all().order_by('-id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'POST' and request.is_ajax(): 
        formu = formCategoria(request.POST)
        if formu.is_valid():
            formu.save()
            idp = categoria.objects.latest('id')            
            historiales(request,["categoria","registrar",idp.id])
            return render(request,'expediente/categoria/ajax_categoria.html',{'lista':categorias,'n':'categoriaU','estado':estado})            
        else:
            return render(request,'expediente/categoria/form_cat.html',{'formu':formu})         
    else:
        formu = formCategoria()
        modulo = {'formu':formu, 'url':'registro_categoria/','n':'categoriaU','estado':estado}
        return paginacion(request,categorias, modulo, 'expediente/categoria/categoria.html' )          

@login_required(login_url='/')
def eliminar_categoria(request):
    categorias = categoria.objects.all().order_by('-id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(categoria,pk=idb).delete()
        historiales(request,["categoria","eliminar",idb])
        return render(request,'expediente/categoria/ajax_categoria.html',{'lista':categorias,'n':'categoriaU','estado':estado})     

@login_required(login_url='/')
def actualizar_categoria(request):
    categorias = categoria.objects.all().order_by('-id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(categoria,pk=idp)
        form=formCategoria(request.POST, instance=a)
        if form.is_valid():
            form.save()
            historiales(request,["categoria","actualizar",idp])
            return render(request,'expediente/categoria/ajax_categoria.html',{'lista':categorias,'n':'categoriaU','estado':estado}) 
        else:
            return render(request,'expediente/categoria/form_cat.html',{'formu':formu})            
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(categoria,pk=idp)
        form= formCategoria(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_categoria/','n':'categoriaU','u':'categoriaU','estado':estado})  


def busq_ajax_ct(request):
    dat = request.GET.get('datos')
    estado =  permi(request, "registro_categoria")
    e = categoria.objects.filter( Q(descripcion__contains=dat))[:10]
    modulo = {'lista':e,'n':'categoriaU','estado':estado}
    return render(request,'expediente/categoria/ajax_categoria.html', modulo)