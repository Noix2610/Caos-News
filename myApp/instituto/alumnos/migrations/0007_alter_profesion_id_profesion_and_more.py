# Generated by Django 4.2.13 on 2024-06-13 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0006_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesion',
            name='id_profesion',
            field=models.AutoField(db_column='id_profesion', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_profesion',
            field=models.ForeignKey(db_column='id_profesion', on_delete=django.db.models.deletion.CASCADE, to='alumnos.profesion'),
        ),
    ]
