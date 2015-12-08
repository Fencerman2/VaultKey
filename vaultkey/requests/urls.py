from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='test'),
    url(r'^$', views.DetailView.as_view(), name='index'),
    url(r'^submit', views.SubmitView.as_view(), name='submitpage')
]
