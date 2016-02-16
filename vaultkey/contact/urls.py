from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CreateView.as_view(), name='index'),
    url(r'^submit/(?P<pk>[0-9]+)/$', views.SubmitView.as_view(), name='sendpage')
]
