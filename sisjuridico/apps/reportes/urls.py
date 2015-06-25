from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps.reportes.views',

	#reportes_consolidados
    url(r'^reportes_consolidados/$', 'reportes_consolidados'),



	)