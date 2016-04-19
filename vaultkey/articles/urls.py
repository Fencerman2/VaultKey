from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='article-detail'),
    url(r'^archive$', views.ArchiveView.as_view(), name='archive')
]
