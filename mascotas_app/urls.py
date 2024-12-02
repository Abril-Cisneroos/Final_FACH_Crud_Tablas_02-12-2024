from django.urls import path
from mascotas_app import views

urlpatterns = [
path("mascotas", views.inicio_vistaMascota, name= "mascotas" ),
path("registrarMascota/",views.registrarMascota,name="registrarMascota"),
    path("seleccionarMascota/<id_mascota>",views.seleccionarMascota,name="seleccionarMascota"),
path("editarMascota/",views.editarMascota,name="editarMascota"),
path("borrarMascota/<id_mascota>",views.borrarMascota,name="borrarMascota"),
]