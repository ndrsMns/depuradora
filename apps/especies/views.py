from django.shortcuts import render, redirect
from .models import Especies
from .form import EspecieNuevaForm, EspeciesForm

def lista_especies(request):
    especies = Especies.objects.all()
    context = {'especies':especies}
    return render(request, 'especies/lista_especies.html', context)

def especie_nueva_form_view(request):
    form =EspecieNuevaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_especies') 
    else:
        form = EspecieNuevaForm()

    context= {'title':'Nueva Especie', 'form':form}
    return render(request, 'especies/agregar_especie.html',context)


def eliminar(request, especie_id):
    especie = Especies.objects.get(id=especie_id)
    especie.delete()
    return redirect ('lista_especies')

def editar(request, especie_id):
    especie = Especies.objects.get(id=especie_id)
    if request.method == 'POST':
        form = EspeciesForm(request.POST, instance=especie)
        if form.is_valid():
            form.save()
            return redirect('lista_especies') 
    else:
        form = EspeciesForm(instance=especie)

    context= {'title':'Eliminar especie', 'form':form}
    return render(request, 'especies/editar_especie.html',context)

