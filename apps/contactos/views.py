from django.shortcuts import render
from .models import Empresa, Contacto
from .form import EmpresaNuevaForm, ContactoNuevoForm


def empresa_nueva_form_view(request):
    form =EmpresaNuevaForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        guardar=Empresa.objects.create(**form.cleaned_data)
        form = EmpresaNuevaForm()
     
    context= {'title':'Nueva Empresa', 'form':form}
    return render(request, 'contactos/form_bootstrap.html',context)

def contacto_nuevo_form_view(request):
    form =ContactoNuevoForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        guardar=Contacto.objects.create(**form.cleaned_data)
        form = ContactoNuevoForm()
    context= {'title':'Nuevo contacto', 'form':form}
    return render(request, 'contactos/form_bootstrap.html',context)
