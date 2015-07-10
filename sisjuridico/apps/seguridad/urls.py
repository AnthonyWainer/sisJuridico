from django.conf.urls import patterns, url, include
from django.contrib.auth.views import password_change,password_change_done
from axes.decorators import watch_login
from .views import Login

urlpatterns = patterns('apps.seguridad.views',


    #url(r'^accounts/', include('django.contrib.auth.urls')),
    
    url(r'^password$', password_change, {'template_name': 'seguridad/cuentas/password.html'}),
    url(r'^password-hecho$', password_change_done, {'template_name': 'seguridad/cuentas/password-hecho.html'},name='password_change_done'),
	#login y logout
    url(r'^$',watch_login(Login)),
    url(r'^salir$', 'LogOut'),

    #principal
	url(r'^sistema$', 'index', name="index"),

    #perfiles
    url(r'^registro_perfil/$', 'registrar_perfil'),
    url(r'^actualizar_perfil/$', 'actualizar_perfil'),
    url(r'^eliminar_perfil/$', 'eliminar_perfil'),

    #usuarios
    url(r'^registro_usuario/$', 'registro_usuario'),
    url(r'^actualizar_usuario/$', 'actualizar_usuario'),
    url(r'^actualizar_info_usuario/$', 'actualizar_info_usuario'),
    url(r'^eliminar_usuario/$', 'eliminar_usuario'),
    url(r'^profile/$', 'profile'),
    url(r'^passDefault/$', 'passDefault'),

    #usuarios bloqueados
    url(r'user_block/','user_block'),
    url(r'busq_ajax_us/','busq_ajax_us'),
    


    #modulos
    url(r'^registro_modulo/$', 'registro_modulo'),
    url(r'^actualizar_modulo/$', 'actualizar_modulo'),
    url(r'^eliminar_modulo/$', 'eliminar_modulo'),

    #submodulos
    url(r'^actualizar_submodulo/$', 'actualizar_submodulo'),
    url(r'^eliminar_submodulo/$', 'eliminar_submodulo'),
    url(r'^registro_submodulo/$', 'registro_submodulo'),
    

    #permisos
    url(r'^registro_permisos/$', 'registro_permisos'),
    url(r'^cambiarEstadoPermiso/$', 'cambiarEstadoPermiso'),
    url(r'^cambiarEstadoPermiso2/$', 'cambiarEstadoPermiso2'),

    #manual
    url(r'^manual/$', 'manual'),    
	)