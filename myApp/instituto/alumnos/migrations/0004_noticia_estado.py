# Generated by Django 4.2.13 on 2024-07-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_noticia_historia2_noticia_textoagregado'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='estado',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
