from django.conf.urls import url
from account import views

urlpatterns =          [url(r'^$', views.login, name='login'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^logout/$', views.logout, name='logout'),
                       url(r'^ErrorMessageAfterLogin/$', views.ErrorMessageAfterLogin, name='ErrorMessageAfterLogin'),
                       url(r'^filter/$', views.filter, name = 'filter'),
                       url(r'^table/$', views.table, name = 'table'),
                       # url(r'^graph/$', views.graph, name='graph'),
                       ]