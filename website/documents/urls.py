from django.conf.urls import url
from . import views

urlpatterns = [
    url('/documents/new_document/', views.new_document, name='new_document'),
]
