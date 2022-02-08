from django.contrib import admin

from .models import Especies

class EspeciesAdmin(admin.ModelAdmin):
    list_display =('fao',
    'n_cientifico',
    'n_comercial',
    'tipo',
    'depuracion')

admin.site.register(Especies, EspeciesAdmin)
