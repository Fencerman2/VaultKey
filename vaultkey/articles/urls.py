from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ArchiveView.as_view(), name='archive'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='article-detail'),
]
