# Generated by Django 4.2.10 on 2025-01-22 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0004_remove_autor_fecha_nacimiento_autor_pais"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="nombre",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
