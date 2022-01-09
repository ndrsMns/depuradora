from django.urls import path
from .views import especie_nueva_form_view, eliminar, lista_especies, editar

app_name = 'especies'

urlpatterns = [
    path('lista_especies/', lista_especies, name='lista_especies'),
    path('agregar_especie/',especie_nueva_form_view, name='agregar_especie'),
    path('eliminar_especie/<int:especie_id>/', eliminar, name='eliminar_especie'),
    path('editar_especie/<int:especie_id>/', editar, name='editar_especie'),
]
