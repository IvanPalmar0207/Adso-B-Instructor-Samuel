# Generated by Django 4.2.6 on 2023-11-14 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitacionesGestion', '0001_initial'),
        ('reservaGestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_reserva',
            name='codigo_hab',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='habitacionesGestion.tb_habitacion', verbose_name='Codigo de la habitacion'),
        ),
    ]
