from django.contrib import admin

from .models import Piscinas, Zonas


class ZonasAdmin(admin.ModelAdmin):
    list_display = ('nombre_zona', 'ubicacion')


class PiscinasAdmin(admin.ModelAdmin):
    list_display = ('no_piscina', 'zona')


admin.site.register(Zonas, ZonasAdmin)
admin.site.register(Piscinas, PiscinasAdmin)
