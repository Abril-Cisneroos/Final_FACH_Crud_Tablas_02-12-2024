# Generated by Django 5.1.2 on 2024-11-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('txtnombre', models.CharField(max_length=50)),
                ('txtcategoria', models.CharField(max_length=50)),
                ('numcantidad', models.PositiveIntegerField()),
                ('txtdescripcion', models.CharField(max_length=200)),
                ('numprecio', models.CharField(max_length=10)),
                ('txtproveedor', models.CharField(max_length=50)),
            ],
        ),
    ]
