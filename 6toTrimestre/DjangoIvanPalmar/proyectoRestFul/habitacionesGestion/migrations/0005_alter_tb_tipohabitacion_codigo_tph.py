# Generated by Django 4.2.6 on 2023-11-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacionesGestion', '0004_alter_tb_estado_codigo_ed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_tipohabitacion',
            name='codigo_tpH',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo del tipo de habitacion'),
        ),
    ]
