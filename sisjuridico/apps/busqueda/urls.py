from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.busqueda.views',

	#busqueda_especifica
	url(r'^busqueda_especifica/$', 'busqueda_especifica'),
    url(r'^busqueda/$', 'busqueda'),



	)