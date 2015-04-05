from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    #url(r'^', include('zinnia.urls.capabilities')),
    url(r'^', include('zinnia.urls', namespace='zinnia')),
]
