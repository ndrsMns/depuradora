from django.urls import path
from .views import empresa_nueva_form_view, contacto_nuevo_form_view
app_name = 'contactos'

urlpatterns = [
    path('formulario_empresa/',empresa_nueva_form_view, name='nueva_empresa'),
    path('formulario_contacto/',contacto_nuevo_form_view, name='nuevo_contacto'),
]
