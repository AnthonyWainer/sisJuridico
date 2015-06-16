from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.matenimiento.views',

	#oficina
    url(r'^registro_oficina/$', 'registro_oficina'),
    url(r'^actualizar_oficina/$', 'actualizar_oficina'),
    url(r'^eliminar_oficina/$', 'eliminar_oficina'),

    #acciones
    url(r'^registro_accion/$', 'registro_accion'),
    url(r'^actualizar_accion/$', 'actualizar_accion'),
    url(r'^eliminar_accion/$', 'eliminar_accion'),
	)