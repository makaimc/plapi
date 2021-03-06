"""plapi URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from languages.views import (api_root, LanguageList, LanguageDetail,
                             LibraryList, LibraryDetail, TutorialDetail,
                             TutorialList)


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^programming-languages/(?P<slug>[a-z0-9\-]+)/$',
        LanguageDetail.as_view(), name='language-detail'),
    url(r'^programming-languages/$', LanguageList.as_view(),
        name="programming-languages"),
    url(r'^libraries/(?P<slug>[a-z0-9\-]+)/$',
        LibraryDetail.as_view(), name='library-detail'),
    url(r'^libraries/$', LibraryList.as_view(),
        name="libraries"),
    url(r'^tutorials/(?P<slug>[a-z0-9\-]+)/$',
        TutorialDetail.as_view(), name='tutorial-detail'),
    url(r'^tutorials/$', TutorialList.as_view(),
        name="tutorials"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', api_root),
]
