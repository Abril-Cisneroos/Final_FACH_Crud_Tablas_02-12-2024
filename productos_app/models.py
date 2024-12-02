from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto = models.PositiveBigIntegerField(null=False, primary_key=True)
    txtnombre = models.CharField(max_length=50, null=False)
    txtcategoria = models.CharField(null=False, max_length=50)
    numcantidad = models.PositiveIntegerField(null=False)
    txtdescripcion = models.CharField(max_length=200)
    numprecio = models.CharField(null=False,max_length=10)
    txtproveedor = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.txtnombre