from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.
def inicio_vistaProducto(request):
    losproductos=Productos.objects.all()
    return render(request,"gestionarProductos.html", {"misProductos":losproductos})

def registrarProducto(request):
    id_producto=request.POST["id_producto"]
    txtnombre=request.POST["txtnombre"]
    txtcategoria=request.POST["txtcategoria"]
    numcantidad=request.POST["numcantidad"]
    txtdescripcion=request.POST["txtdescripcion"]
    numprecio=request.POST["numprecio"]
    txtproveedor=request.POST["txtproveedor"]
    
    guardarProducto=Productos.objects.create(
        id_producto=id_producto,txtnombre=txtnombre,txtcategoria=txtcategoria,numcantidad=numcantidad,txtdescripcion=txtdescripcion,
        numprecio=numprecio,txtproveedor=txtproveedor
    ) #GUARDA EL REGISTRO
    
    return redirect("productos")

def seleccionarProducto(request,id_producto):
    producto=Productos.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html",{"misProductos":producto})

def editarProducto(request):
    id_producto=request.POST["id_producto"]
    txtnombre=request.POST["txtnombre"]
    txtcategoria=request.POST["txtcategoria"]
    numcantidad=request.POST["numcantidad"]
    txtdescripcion=request.POST["txtdescripcion"]
    numprecio=request.POST["numprecio"]
    txtproveedor=request.POST["txtproveedor"]
    
    producto=Productos.objects.get(id_producto=id_producto)
    producto.id_producto=id_producto
    producto.txtnombre=txtnombre
    producto.txtcategoria=txtcategoria
    producto.numcantidad=numcantidad
    producto.txtdescripcion=txtdescripcion
    producto.numprecio=numprecio
    producto.txtproveedor=txtproveedor
    producto.save() #guarda registro actualizado
    return redirect("productos")

def borrarProducto(request,id_producto):
    productos=Productos.objects.get(id_producto=id_producto)
    productos.delete() # borra el registro
    return redirect("productos")