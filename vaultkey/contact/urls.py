from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CreateView.as_view(), name='index'),
    url(r'^send/(?P<pk>[0-9]+)/$', views.SendView.as_view(), name='submitpage')
]
