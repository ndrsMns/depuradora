# Generated by Django 4.0.1 on 2022-01-13 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0002_alter_empresa_options_empresa_rgsea_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='codigo',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True, verbose_name='Código de proveedor'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='proveedor_aprobado',
            field=models.BooleanField(default=False, verbose_name='¿Proveedor aprobado?'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='contactos.empresa'),
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('contactos.empresa',),
        ),
    ]
