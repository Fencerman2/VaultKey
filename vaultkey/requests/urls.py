from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CreateView.as_view(), name='index'),
    url(r'^alter-request/$', views.SubmitView.as_view(), name='submitpage')
]
