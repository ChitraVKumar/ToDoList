from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>[\w-]+)/$', views.details, name='details'),
    url(r'^add', views.add, name='add'),
    url(r'^complete/(?P<id>\d+)', views.complete, name='complete'),
    url(r'^delete/(?P<id>\d+)', views.delete, name='delete'),
]
