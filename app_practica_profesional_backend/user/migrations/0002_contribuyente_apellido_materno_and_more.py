# Generated by Django 5.1.5 on 2025-01-29 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribuyente',
            name='apellido_materno',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='contribuyente',
            name='apellido_paterno',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AlterField(
            model_name='contribuyente',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
