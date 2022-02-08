from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from .models import Zonas, Piscinas
from .forms import PiscinasForm, ZonasForm


class PiscinasCreateView(CreateView):
    model = Piscinas
    template_name = "piscinas/editar_elemento.html"
    fields = '__all__'
    success_url = reverse_lazy('piscinas:lista-piscinas')



class PiscinasDetailView(DetailView):
    model = Piscinas
    template_name = "piscinas/detalle_piscina.html"
    fields = '--all--'
    exclude = []
    context_object_name = 'piscina'


class PiscinasListView(ListView):
    model = Piscinas
    template_name = 'piscinas/lista_piscinas.html'
    context_object_name = 'piscinas'


class PiscinasUpdateView(UpdateView):
    model = Piscinas
    template_name = "piscinas/editar_elemento.html"
    fields = '__all__'
    success_url = 'piscinas/lista_piscinas/'
    class_form = PiscinasForm


class PiscinasDeleteView(DeleteView):
    model = Piscinas
    template_name = "piscinas/eliminar_elemento.html"
    success_url = "piscinas:lista-piscinas"


class ZonasCreateView(CreateView):
    model = Zonas
    template_name = "piscinas/editar_elemento.html"
    exclude = []
    fields = '__all__'
    success_url = reverse_lazy('piscinas:lista-zonas')


class ZonasDetailView(DetailView):
    model = Zonas
    template_name = "piscinas/detalle_zona.html"
    context_object_name = 'zonas'
    #fields = model._meta.get_fields()

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['fields'] = Zonas._meta.get_fields()
        return context


class ZonasListView(ListView):
    model = Zonas
    template_name = 'piscinas/lista_zonas.html'
    context_object_name = 'zonas'


class ZonasUpdateView(UpdateView):
    model = Zonas
    template_name = "piscinas/editar_elemento.html"
    fields = '__all__'
    success_url = reverse_lazy('piscinas:lista-zonas')


class ZonasDeleteView(DeleteView):
    model = Zonas
    template_name = "piscinas/eliminar_elemento.html"
    success_url = reverse_lazy('piscinas:lista-zonas')
