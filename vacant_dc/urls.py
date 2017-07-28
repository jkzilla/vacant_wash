from django.conf.urls import url
from . import views

app_name = 'vacant_dc'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^form/$', views.FormView.as_view(), name='form'),
]