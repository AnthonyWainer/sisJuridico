from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.seguridad.views',

	#este es mi primer index
	url(r'^sistema$', 'index', name="index"),




	)