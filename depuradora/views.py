from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context={'title': 'Página principal', 'empresa':'MercaMaris Costa da Morte, S.L.' }
    return render(request, 'index.html', context)
