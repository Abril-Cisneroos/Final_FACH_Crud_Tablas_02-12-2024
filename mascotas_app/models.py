from django.db import models

# Create your models here.
class Mascotas(models.Model):
    id_mascota = models.PositiveBigIntegerField(null=False, primary_key=True)
    txtnombre = models.CharField(max_length=50, null=False)
    txtespecie = models.CharField(null=False, max_length=50)
    numedad = models.PositiveIntegerField(null=False)
    numpeso = models.FloatField()
    id_cliente = models.CharField(null=False,max_length=10)
    txthistorial = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.txtnombre