from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from apps.seguridad.models import permisos
from apps.expediente.models import expedientes, categoria, resolucion
import json as simplejson
import datetime
today  = datetime.datetime.now()
fecha   = today.strftime("%Y-%m-%d") 


# Crea tus vista aqui.
def permi(request,url):
    idp = request.user.idperfil_id
    mod = permisos.objects.filter(idmodulo__url=url, idperfil_id=idp).values('idmodulo__url','buscar','eliminar','editar','insertar','imprimir','ver')
    return mod

@login_required(login_url='/')
def reportes_consolidados(request):
    if request.method == 'POST': 
        e = expedientes.objects.filter(fecha__range= [request.POST["fecha_ini"],request.POST["fecha_ter"]])
        ep = 0
        a  = 0        
        na = 0
        for i in e:
            if i.estado == "en proceso":
                ep += 1
            elif i.estado == "aprobado":
                a += 1
            elif i.estado == "no aprobado":
                na += 1
        if request.POST["v"] == "v":
            data = []
            data.append({"label":"Aprobado","data":a,"color": "#d3d3d3",})
            data.append({"label":"No Aprobado","data":na,"color": "#79d2c0",})
            data.append({"label":"En Proceso","data":ep,"color": "#1ab394",})
            return HttpResponse(simplejson.dumps(data), content_type="application/json" )

        return render(request,"reportes/reportes_consolidados/ajax_reportes_consolidados.html",{'ep':ep,'ap':a,'na':na})

    return render(request,"reportes/reportes_consolidados/reportes_consolidados.html",{'fecha':fecha})

@login_required(login_url='/')
def reportes_detallados(request):
    estado =  permi(request, "reportes_detallados")
    listaCategoria = [{'id':con.id,'descripcion':con.descripcion} for con in categoria.objects.all()]
    listaResolucion = [{'id':con.id,'numero':con.numero} for con in resolucion.objects.all()]

    if request.method == 'POST': 
        idc = request.POST.get("idc","")
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('id')  
        return render(request,'reportes/reportes_detallados/ajax_reportes_detallados.html',{'lista':expediente,'estado':estado})            
    else:    
        idc= 1
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('id')
        modulo = {'lista':expediente, 'url':'reportes_detallados/','n':'reportesU','estado':estado,'idcategoria':listaCategoria, 'idresolucion':listaResolucion,'fecha' :fecha}
        return render(request,  'reportes/reportes_detallados/reportes_detallados.html',modulo )        

def busqueda(request):
    e = expedientes.objects.filter( Q(nro__contains=request.POST["nro"]), Q(idcategoria__id__contains=request.POST["idcategoria"]), Q(fecha__contains=request.POST["fecha"]), Q(estado__contains=request.POST["estado"]) )[:10]
    print (e.query)
    modulo = {'lista':e}
    return render(request,'reportes/reportes_detallados/ajax_reportes_detallados.html', modulo)