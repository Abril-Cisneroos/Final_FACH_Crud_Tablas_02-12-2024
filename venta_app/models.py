from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_venta = models.PositiveBigIntegerField(null=False, primary_key=True)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField(null=False)
    precio = models.FloatField(null=False)
    id_cliente = models.PositiveSmallIntegerField(null=False)
    id_empleado = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return self.id_venta