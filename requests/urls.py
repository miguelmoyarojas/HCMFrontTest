# -*- encoding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/(?P<view_type>[0-9]+)/$', views.index, name='index'),
    url(r'^view_vacant/(?P<request_id>[0-9]+)/$', views.view_vacant, name='view_vacant'),
    url(r'^view_vacation/(?P<request_id>[0-9]+)/$', views.view_vacation, name='view_vacation'),
    url(r'^new_vacant/$', views.new_vacant, name='new_vacant'),
    url(r'^new_vacation/$', views.new_vacation, name='new_vacation'),
    url(r'^delete_vacant/(?P<request_id>[0-9]+)/$', views.delete_vacant, name='delete_vacant'),
    url(r'^delete_vacation/(?P<request_id>[0-9]+)/$', views.delete_vacation, name='delete_vacation'),
    url(r'^approve_vacant/(?P<request_id>[0-9]+)/$', views.approve_vacant, name='approve_vacant'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view')
]
