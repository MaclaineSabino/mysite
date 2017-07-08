"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pools import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^question/(?P<pk>\d+)$',views.exibir, name='questaodet'),
    url(r'^question/(?P<pk>\d+)/results/$',views.results, name='results'),
    url(r'^question/(?P<pk>\d+)/vote/$',views.vote, name='voto'),
    url(r'^question/(?P<pk>\d+)/manage/$',views.manage, name='manage'),
    url(r'^question/(?P<pk>\d+)/status/$',views.status, name='status'),
    url(r'^question/(?P<pk>\d+)/remover/$',views.remover, name='remover'),
    url(r'^question/(?P<pk>\d+)/incluir/(?P<pkc>\d+)$',views.incluir, name='incluir')
]
