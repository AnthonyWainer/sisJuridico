from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.expediente.views',

	#este es mi primer index
    url(r'^registro_expediente$', 'registro_expediente'),
    url(r'^registro_categoria$', 'registro_categoria'),

	)