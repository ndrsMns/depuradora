# Generated by Django 4.0.1 on 2022-01-07 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AddField(
            model_name='empresa',
            name='rgsea',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='RGSEAA'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='contactos.empresa'),
        ),
    ]