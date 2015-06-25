from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.seguridad.models import permisos
from apps.expediente.models import expedientes
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
            #print data
            return HttpResponse(simplejson.dumps(data), content_type="application/json" )
        return render(request,"reportes/reportes_consolidados/ajax_reportes_consolidados.html",{'ep':ep,'ap':a,'na':na})

    return render(request,"reportes/reportes_consolidados/reportes_consolidados.html",{'fecha':fecha})
