from django.urls import path
from .views import (
    PiscinasListView,
    PiscinasCreateView,
    PiscinasUpdateView,
    PiscinasDeleteView,
    PiscinasDetailView,
    ZonasListView,
    ZonasCreateView,
    ZonasUpdateView,
    ZonasDeleteView,
    ZonasDetailView,
)


app_name = 'apps.piscinas'

urlpatterns = [
    path('piscinas/lista/',
         PiscinasListView.as_view(),
         name='lista-piscinas'),
    path('piscinas/<int:pk>/detalle/',
         PiscinasDetailView.as_view(extra_context={'title': 'Piscina'}),
         name='detalle-piscina'),
    path('nueva_piscina/',
         PiscinasCreateView.as_view(extra_context={'title': 'Nueva piscina'}),
         name='nueva-piscina'),
    path('piscinas/<int:pk>/editar/',
         PiscinasUpdateView.as_view(extra_context={'title': 'Modificar piscina'}),
         name='editar-piscina'),
    path('piscinas/<int:pk>/eliminar/',
         PiscinasDeleteView.as_view(extra_context={'title': 'Eliminar piscina'}),
         name='eliminar-piscina'),
    path('zonas/lista/',
         ZonasListView.as_view(), name='lista-zonas'),
    path('zonas/<int:pk>/detalle/',
         ZonasDetailView.as_view(extra_context={'title': 'Zona'}),
         name='detalle-zona'),
    path('nueva_zona/',
         ZonasCreateView.as_view(extra_context={'title': 'Nueva zona'}),
         name='nueva-zona'),
    path('zonas/<int:pk>/editar/',
         ZonasUpdateView.as_view(extra_context={'title': 'Modificar zona'}),
         name='editar-zona'),
    path('zonas/<int:pk>/eliminar/',
         ZonasDeleteView.as_view(extra_context={'title': 'Eliminar zona'}),
         name='eliminar-zona'),
]
