from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.shortcuts import render


from .models import DocRegistro, EntradaBivalvosDepuracion


class DocRegistroListView(ListView):
    model = DocRegistro
    template_name = "bivalvos/doc_reg_list.html"


