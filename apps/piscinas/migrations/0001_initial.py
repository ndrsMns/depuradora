# Generated by Django 4.0.1 on 2022-01-11 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_zona', models.CharField(max_length=30, verbose_name='Nombre Zona')),
                ('ubicacion', models.CharField(max_length=100, verbose_name='Ubicación')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'ordering': ['nombre_zona'],
            },
        ),
        migrations.CreateModel(
            name='Piscinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_piscina', models.CharField(max_length=30, verbose_name='Número piscina')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piscinas.zonas')),
            ],
            options={
                'verbose_name': 'Piscina',
                'verbose_name_plural': 'Piscinas',
                'ordering': ['no_piscina'],
            },
        ),
    ]