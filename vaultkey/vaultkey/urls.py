"""vaultkey URL Configuration

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
from material.frontend import urls as frontend_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'home.views.index'),
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^request/', include('alters.urls')),
    url(r'^player/', include('player.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'', include(frontend_urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
