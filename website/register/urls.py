from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^client_employee/$', views.register_ClientEmployee_part1, name='register_ClientEmployee_part1'),
    url(r'^client_employee/(?P<perfil_id>\d+)/$', views.register_ClientEmployee_part2, name='register_ClientEmployee_part2'),
    url(r'^ey_employee/$', views.register_EyEmployee_part1, name='register_EyEmployee_part1'),
    url(r'^ey_employee/(?P<perfil_id>\d+)/$', views.register_EyEmployee_part2, name='register_EyEmployee_part2'),
    url(r'^project_ey_employee/$', views.project_ey_employee, name='project_ey_employee'),
    url(r'^project_client_employee/$', views.project_client_employee, name='project_client_employee'),
    url(r'^$', views.register, name='register'),
]
