# Generated by Django 4.2.6 on 2023-11-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_dasd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correoElectronico_clI', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
            ],
        ),
        migrations.CreateModel(
            name='tb_rol',
            fields=[
                ('codigo_rl', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo del rol')),
                ('tipo_rl', models.CharField(max_length=50, verbose_name='Tipo de rol')),
            ],
        ),
        migrations.CreateModel(
            name='tb_tpDocumento',
            fields=[
                ('codigo_tpD', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo del tipo de documento')),
                ('tipo_tpDD', models.CharField(max_length=60, verbose_name='Tipo de documento')),
                ('abreviatura_tpD', models.CharField(max_length=50, verbose_name='Abreviatura del tipo de documento')),
            ],
        ),
        migrations.CreateModel(
            name='tb_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrasena_cli', models.CharField(max_length=50, verbose_name='Contraseña del usuario')),
                ('codigo_rl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuariosGestion.tb_rol', verbose_name='Codigo de rol')),
                ('codigo_tpD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuariosGestion.tb_tpdocumento', verbose_name='Codigo del tipo de documento')),
            ],
        ),
    ]