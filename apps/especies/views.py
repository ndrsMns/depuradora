from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Especies
from .form import EspecieNuevaForm, EspeciesForm


def lista_especies(request):
    especies = Especies.objects.all()
    paginator = Paginator(especies, 6) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #context = {'especies': especies}
    return render(request, 'especies/lista_especies.html', {'page_obj': page_obj})


def especie_nueva_form_view(request):
    form = EspecieNuevaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_especies')
    else:
        form = EspecieNuevaForm()

    context = {'title': 'Nueva Especie', 'form': form}
    return render(request, 'especies/agregar_especie.html', context)


def eliminar(request, especie_id):
    especie = Especies.objects.get(id=especie_id)
    especie.delete()
    return redirect('especies:lista_especies')


def editar(request, especie_id):
    especie = Especies.objects.get(id=especie_id)
    if request.method == 'POST':
        form = EspeciesForm(request.POST, instance=especie)
        if form.is_valid():
            form.save()
            return redirect('especies:lista_especies')
    else:
        form = EspeciesForm(instance=especie)

    context = {'title': 'Eliminar especie', 'form': form}
    return render(request, 'especies/editar_especie.html', context)
