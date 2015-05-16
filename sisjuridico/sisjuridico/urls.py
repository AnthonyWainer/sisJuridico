from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [ 
    # Examples:
    # url(r'^$', 'clase1.views.home', name='home'),
    url(r'^', include('apps.app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
