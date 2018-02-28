from django.urls import path

from . import views
from api.views import ListCreateObjects
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('objects/', ListCreateObjects.as_view(), name='list_objects')
]