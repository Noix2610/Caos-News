# Generated by Django 4.2.13 on 2024-07-13 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0008_remove_usuario_apellidos_remove_usuario_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumnos.region'),
        ),
    ]
