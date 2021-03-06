from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [ 
    # Examples:
    # url(r'^$', 'clase1.views.home', name='home'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    url(r'^', include('apps.busqueda.urls')),
    url(r'^', include('apps.expediente.urls')),
    url(r'^', include('apps.matenimiento.urls')),
    url(r'^', include('apps.reportes.urls')),
    url(r'^', include('apps.seguridad.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
