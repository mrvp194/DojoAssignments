from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^users/$', views.index, name='index'),    
    url(r'^users/new$', views.new, name='new'),
    url(r'^users/create$', views.create, name='create'),
    url(r'^users/(?P<id>\w+)/show$', views.show, name='show'),
    url(r'^users/(?P<id>\w+)/edit$', views.edit, name='edit'),
    url(r'^users/(?P<id>\w+)/update$', views.update, name='update'),
    url(r'^users/(?P<id>\w+)/delete$', views.destroy, name='destroy'),
]