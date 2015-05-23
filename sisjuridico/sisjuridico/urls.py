from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [ 
    # Examples:
    # url(r'^$', 'clase1.views.home', name='home'),
    url(r'^', include('apps.busqueda.urls')),
    url(r'^', include('apps.expediente.urls')),
    url(r'^', include('apps.matenimiento.urls')),
    url(r'^', include('apps.reportes.urls')),
    url(r'^', include('apps.seguridad.urls',namespace="apps.seguridad")),
    url(r'^', include('apps.cuentas.urls',namespace="cuentas")),
    url(r'^users/', include('profiles.urls',namespace="profiles")),
    url(r'^admin/', include(admin.site.urls)),
]
