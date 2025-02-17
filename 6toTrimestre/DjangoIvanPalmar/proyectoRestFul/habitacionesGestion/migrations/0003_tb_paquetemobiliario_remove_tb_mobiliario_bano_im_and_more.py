# Generated by Django 4.2.6 on 2023-11-29 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitacionesGestion', '0002_remove_tb_habitacion_precio_tph'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_paqueteMobiliario',
            fields=[
                ('codigo_pMb', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Codigo del paquete')),
                ('paqueteTipo_pMb', models.CharField(max_length=70, verbose_name='Tipo de paquete')),
                ('camasSecillas_pMb', models.IntegerField(verbose_name='Numero de camas sencillas')),
                ('camasDobles_pMb', models.IntegerField(verbose_name='Numero de camas dobles')),
                ('camasTriples_pMb', models.IntegerField(verbose_name='Numero de camas triples')),
                ('numeroTelevisores_pMb', models.IntegerField(verbose_name='Numero de televisores')),
                ('numeroBanos_pMb', models.IntegerField(verbose_name='Numero de baños')),
                ('numeroToallas_pMb', models.IntegerField(verbose_name='Numero de toallas')),
                ('numeroTocadores', models.IntegerField(verbose_name='Numero de tocadores')),
            ],
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='bano_im',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='camasDobles_im',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='camasMatrimoniales_im',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='camasSecillas_im',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='camasTriples_im',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='escritorio_im',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tb_mobiliario',
            name='televisor_im',
        ),
        migrations.AddField(
            model_name='tb_mobiliario',
            name='codigo_mB',
            field=models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Codigo del mobiliario'),
        ),
        migrations.AlterField(
            model_name='tb_mobiliario',
            name='codigo_tpH',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='habitacionesGestion.tb_tipohabitacion', verbose_name='Codigo del tipo de habitacion'),
        ),
        migrations.AddField(
            model_name='tb_mobiliario',
            name='codigo_pMb',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='habitacionesGestion.tb_paquetemobiliario', verbose_name='Codigo del parquete de mobiliario'),
        ),
    ]
