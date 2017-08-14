from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_all),
    url(r'^blogs/?$', views.index),
    url(r'^blogs/create/?$', views.create),
    url(r'^blogs/new/?$', views.new),
    url(r'^blogs/(?P<blog_id>\d{1,10})/?$', views.show),
    url(r'^blogs/(?P<blog_id>\d{1,10})/edit/?$', views.edit),
    url(r'^blogs/(?P<blog_id>\d{1,10})/delete/?$', views.destroy),
]