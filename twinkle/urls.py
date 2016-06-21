"""Starry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from twinkle import views


urlpatterns = [
    url(r'^$', views.twinkle_list, name='twinkle_list'),
    #url(r'^$', views.PostListView.as_view(), name='twinkle_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<slug>[-\w]+)/$',
    views.twinkle_detail,name='twinkle_detail'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.twinkle_list,
        name='twinkle_list_by_tag'),

]
