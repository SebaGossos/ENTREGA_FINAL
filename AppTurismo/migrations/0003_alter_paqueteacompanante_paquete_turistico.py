# Generated by Django 4.1.1 on 2022-10-02 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurismo', '0002_alter_paqueteacompanante_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paqueteacompanante',
            name='paquete_turistico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppTurismo.paqueteturistico'),
        ),
    ]