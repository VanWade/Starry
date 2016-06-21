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
from django.contrib.sitemaps.views import sitemap
from twinkle.sitemaps import TwinkleSitemap
from django.contrib.auth.views import login,logout,logout_then_login,password_change,password_change_done
from twinkle import views
sitemaps = {
    'twinkles': TwinkleSitemap,
}
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^twinkle/', include('twinkle.urls',namespace='twinkle',app_name='twinkle')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^logout-then-login/$',logout_then_login,
        name='logout_then_login'),
    url(r'^$',views.dashboard,name='dashboard'),
    url(r'^password-change/$',password_change,name='password_change'),
    url(r'^password-change/done/$',password_change_done,name='password_change_done'),
]

