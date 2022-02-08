from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin

from .models import Contacto, Empresa, Proveedor


class EmpresaResource(resources.ModelResource):
    class Meta:
        model = Empresa


class EmpresaAdmin(ImportExportModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('denominacion',
                       'n_comercial',
                       'calle',
                       'nif',
                       'rgsea',
                       'cliente',
                       'proveedor',
                       )
        }),
        ('Dirección', {
            'classes': ('collapse',),
            'fields': ('calle2',
                       'ciudad',
                       'provincia',
                       'cp',
                       'pais',
                       'email',
                       'tfno',
                       'movil'),
        }),
    )
    resource_class = EmpresaResource
    search_fields = ('denominacion', 'n_comercial')
    list_display = ('denominacion',
                    'n_comercial',
                    'nif',
                    'provincia',
                    )
    list_display_links = ('n_comercial',
                          'nif',
                          'provincia')


class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor


class ProveedorAdmin(ImportExportModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('denominacion',
                       'n_comercial',
                       'rgsea',
                       'codigo',
                       'cliente',
                       'proveedor',
                       'proveedor_aprobado',
                       )
        }),
        ('Dirección', {
            'classes': ('collapse',),
            'fields': ('calle2',
                       'ciudad',
                       'provincia',
                       'cp',
                       'pais',
                       'email',
                       'tfno',
                       'movil'),
        }),
    )
    resource_class = EmpresaResource
    search_fields = ('denominacion', 'n_comercial')
    list_display = ('n_comercial',
                    'codigo',
                    'nif',
                    'provincia',
                    )
    list_display_links = ('n_comercial',
                          'nif',
                          'provincia')


class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto


class ContactoAdmin(ImportExportModelAdmin):
    resource_class = ContactoResource
    search_fields = ('empresa', 'nombre')
    list_display = ('nombre',
                    'empresa',
                    'email',
                    'tfno',
                    )
    list_display_links = ('nombre',
                          'empresa',
                          )


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
