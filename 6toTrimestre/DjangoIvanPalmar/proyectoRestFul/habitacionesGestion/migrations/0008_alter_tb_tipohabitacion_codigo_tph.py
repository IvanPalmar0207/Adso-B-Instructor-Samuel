# Generated by Django 4.2.6 on 2023-12-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacionesGestion', '0007_alter_tb_tipohabitacion_codigo_tph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_tipohabitacion',
            name='codigo_tpH',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo del tipo de habitacion'),
        ),
    ]
