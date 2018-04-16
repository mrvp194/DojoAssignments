from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\w+)$', views.show),
    url(r'^(?P<id>\w+)/edit$', views.edit),
    url(r'^(?P<id>\w+)/delete$', views.destroy),

]