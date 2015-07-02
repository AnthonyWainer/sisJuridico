from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.reportes.views',

	#reportes_consolidados
    url(r'^reportes_consolidados/$', 'reportes_consolidados'),
    url(r'^reportes_detallados/$', 'reportes_detallados'),
    url(r'^reportes_transacciones/$', 'reportes_transacciones'),
    url(r'^reportes/$', 'busqueda'),
    url(r'^reportesT/$', 'transacciones'),



	)