from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.expediente.views',

	#este es mi primer index
    url(r'^registro_expediente/$', 'registro_expediente'),
    url(r'^actualizar_expediente/$', 'actualizar_expediente'),
    url(r'^eliminar_expediente/$', 'eliminar_expediente'),
    url(r'^busq_ajax_exp/$', 'busq_ajax_exp'),
    

    #categoria
    url(r'^registro_categoria/$', 'registro_categoria'),
    url(r'^actualizar_categoria/$', 'actualizar_categoria'),
    url(r'^eliminar_categoria/$', 'eliminar_categoria'),
    url(r'^busq_ajax_ct/$', 'busq_ajax_ct'),

    #hoja de envio
    url(r'^registro_hoja_envio/$', 'registro_hoja_envio'),
    url(r'^actualizar_hoja_envio/$', 'actualizar_hoja_envio'),
    url(r'^eliminar_hoja_envio/$', 'eliminar_hoja_envio'),

    #resolucion
    url(r'^registro_resolucion/$', 'registro_resolucion'),
    url(r'^actualizar_resolucion/$', 'actualizar_resolucion'),
    url(r'^eliminar_resolucion/$', 'eliminar_resolucion'),
    url(r'^busq_ajax_re/$', 'busq_ajax_re'),
    




	)