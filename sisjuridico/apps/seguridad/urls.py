from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.seguridad.views',

	#este es mi primer index
	url(r'^sistema$', 'index', name="index"),
    url(r'^registro_permisos/$', 'permisos'),
    url(r'^registro_perfil/$', 'registrar_perfil'),
    url(r'^actualizar_perfil/$', 'actualizar_perfil'),
    url(r'^eliminar_perfil/$', 'eliminar_perfil'),
    url(r'^$','Login' ),
    url(r'^salir$', 'LogOut'),
    

	)