from django.contrib import admin
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^Events$', views.events, name='event'),
   
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    