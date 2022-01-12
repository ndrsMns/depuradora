from django.shortcuts import render, redirect
from .models import Empresa, Contacto
from .form import EmpresaNuevaForm, ContactoNuevoForm, ContactoForm

def lista_contactos(request):
    contactos = Contacto.objects.all()
    context = {'contactos':contactos}
    return render(request, 'contactos/lista_contactos.html', context)

def contacto_nuevo_form_view(request):
    form =ContactoNuevoForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        guardar = Contacto.objects.create(**form.cleaned_data)
        form = ContactoNuevoForm()
    context= {'title':'Nuevo contacto', 'form':form}
    return render(request, 'contactos/agregar_contacto.html',context)

def eliminar_contacto (request, contacto_id):
    contacto = Contacto.objects.get(id = contacto_id)
    contacto.delete()
    return redirect ('lista_contactos')


def editar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id = contacto_id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance = contacto)
        if form.is_valid():
            form.save()
            return redirect('contactos:lista_contactos') 
    else:
        form = ContactoForm(instance = contacto)

    context= {'title':'Editar contacto', 'form':form}
    return render(request, 'contactos/editar_contacto.html',context)


def empresa_nueva_form_view(request):
    form = EmpresaNuevaForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        guardar=Empresa.objects.create(**form.cleaned_data)
        form = EmpresaNuevaForm()
     
    context= {'title':'Nueva Empresa', 'form':form}
    return render(request, 'contactos/agregar_empresa.html',context)


