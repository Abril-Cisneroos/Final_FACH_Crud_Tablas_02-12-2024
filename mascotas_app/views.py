from django.shortcuts import render, redirect
from .models import Mascotas

# Create your views here.
def inicio_vistaMascota(request):
    losMascotas=Mascotas.objects.all()
    return render(request,"gestionarMascotas.html", {"misMascotas":losMascotas})

def registrarMascota(request):
    id_mascota=request.POST["id_mascota"]
    txtnombre=request.POST["txtnombre"]
    txtespecie=request.POST["txtespecie"]
    numedad=request.POST["numedad"]
    numpeso=request.POST["numpeso"]
    id_cliente=request.POST["id_cliente"]
    txthistorial = request.POST["txthistorial"]
    
    guardarMascota=Mascotas.objects.create(
        id_mascota=id_mascota,txtnombre=txtnombre,txtespecie=txtespecie,numedad=numedad,
        numpeso=numpeso,id_cliente=id_cliente,txthistorial=txthistorial
    ) #GUARDA EL REGISTRO
    
    return redirect("mascotas")

def seleccionarMascota(request,id_mascota):
    mascota=Mascotas.objects.get(id_mascota=id_mascota)
    return render(request, "editarMascotas.html",{"misMascotas":mascota})

def editarMascota(request):
    id_mascota=request.POST["id_mascota"]
    txtnombre=request.POST["txtnombre"]
    txtespecie=request.POST["txtespecie"]
    numedad=request.POST["numedad"]
    numpeso=request.POST["numpeso"]
    id_cliente=request.POST["id_cliente"]
    txthistorial = request.POST["txthistorial"]
    
    mascota=Mascotas.objects.get(id_mascota=id_mascota)
    mascota.id_mascota=id_mascota
    mascota.txtnombre=txtnombre
    mascota.txtespecie=txtespecie
    mascota.numedad=numedad
    mascota.numpeso=numpeso
    mascota.id_cliente=id_cliente
    mascota.txthistorial=txthistorial
    mascota.save() #guarda registro actualizado
    return redirect("mascotas")

def borrarMascota(request,id_mascota):
    mascotas=Mascotas.objects.get(id_mascota=id_mascota)
    mascotas.delete() # borra el registro
    return redirect("mascotas")