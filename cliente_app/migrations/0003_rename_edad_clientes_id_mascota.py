# Generated by Django 5.1.1 on 2024-12-02 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_app', '0002_alter_clientes_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='edad',
            new_name='id_mascota',
        ),
    ]
