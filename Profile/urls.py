from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User


from Profile import views

urlpatterns = [
    
    re_path(r'Profile_List/$', views.ProfileList.as_view()),
    re_path(r'Ciudad_List/$', views.CiudadList.as_view()),
    re_path(r'Genero_List/$', views.GeneroList.as_view()),
    re_path(r'Ocupacion_List/$', views.OcupacionList.as_view()),
    re_path(r'Estado_List/$', views.EstadoList.as_view()),
    re_path(r'Estadocivil_List/$', views.EstadocivilList.as_view())
]