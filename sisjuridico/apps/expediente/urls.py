from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.expediente.views',

	#este es mi primer index
    url(r'^registro_expediente/$', 'registro_expediente'),
    url(r'^actualizar_expediente/$', 'actualizar_expediente'),
    url(r'^eliminar_expediente/$', 'eliminar_expediente'),

    #categoria
    url(r'^registro_categoria/$', 'registro_categoria'),
    url(r'^actualizar_categoria/$', 'actualizar_categoria'),
    url(r'^eliminar_categoria/$', 'eliminar_categoria'),

    #hoja de envio
    url(r'^registro_hoja_envio/$', 'registro_hoja_envio'),

    #resolucion
    url(r'^registro_resolucion/$', 'registro_resolucion'),




	)