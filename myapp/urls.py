from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^handel-form/$', views.handel_form, name='handel_form'),
]