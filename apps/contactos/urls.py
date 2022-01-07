from django.urls import path
from .views import empresa_nueva_form_view, contacto_nuevo_form_view

urlpatterns = [
    path('formulario_empresa/',empresa_nueva_form_view, name='empresa'),
    path('formulario_contacto/',contacto_nuevo_form_view, name='contacto'),
]
