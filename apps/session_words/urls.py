from django.conf.urls import url

from . import views

urlpattern = [
    url(r'^$', views.index),
    url(r'^add_word/?$', views.add_word),
    url(r'clear/?$', views.clear),
]