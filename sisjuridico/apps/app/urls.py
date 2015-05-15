from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.app.views',

	#este es mi primer index
	url(r'^$', 'index'),
    url(r'^hora/$', 'hora_actual'),


	)