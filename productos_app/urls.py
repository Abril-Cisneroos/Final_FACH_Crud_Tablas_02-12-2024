from django.urls import path
from productos_app import views

urlpatterns = [
path("productos", views.inicio_vistaProducto, name= "productos" ),
path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<id_producto>",views.seleccionarProducto,name="seleccionarProducto"),
path("editarProducto/",views.editarProducto,name="editarProducto"),
path("borrarProducto/<id_producto>",views.borrarProducto,name="borrarProducto"),
]