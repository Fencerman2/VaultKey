from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DetailView.as_view(), name='index'),
]
