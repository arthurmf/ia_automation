from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/', views.new, name='new'),
    url(r'^(?P<perfil_id>\d+)', views.step, name='step'),
]
