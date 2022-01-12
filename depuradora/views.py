from django.shortcuts import render


def home(request):
    context = {'title': 'Página principal',
               'empresa': 'MercaMaris Costa da Morte, S.L.'}
    return render(request, 'index.html', context)
