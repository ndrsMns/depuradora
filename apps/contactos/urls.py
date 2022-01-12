from django.urls import path
from .views import (empresa_nueva_form_view, 
                    contacto_nuevo_form_view, 
                    lista_contactos, 
                    eliminar_contacto, 
                    editar_contacto
                    )

app_name = 'contactos'

urlpatterns = [
    path('formulario_empresa/',empresa_nueva_form_view, name='nueva_empresa'),
    path('formulario_contacto/',contacto_nuevo_form_view, name='nuevo_contacto'),
    path('lista_contactos/', lista_contactos, name='lista_contactos'),
    path('eliminar_contacto/<int:contacto_id>/', eliminar_contacto, name='eliminar_contacto'),
    path('editar_contacto/<int:contacto_id>/',editar_contacto, name='editar_contacto'),
]
