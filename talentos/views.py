from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Talento
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache


def index(request):

    return redirect('talentos')
 
def talentos(request):
    talentos_list = Talento.objects.order_by('nome')
    filtered_talentos = talentos_list
    if request.method == 'POST':
        id = request.POST.get('id')
        if id == 'UXD':
            filtered_talentos = Talento.objects.filter(is_uxdesigner=True)
        elif id == 'UID':
            filtered_talentos = Talento.objects.filter(is_uidesigner=True)
        elif id == 'UXW':
            filtered_talentos = Talento.objects.filter(is_uxwriter=True)
        else:
            filtered_talentos = Talento.objects.order_by('nome')

        return redirect('filter-talentos', id=id)
    else:
        return render(request, 'talentos.html', {'talentos': filtered_talentos})


def filter_talentos(request, id):
    talentos_list = Talento.objects.order_by('nome')
    filtered_talentos = talentos_list

    filtered_talentos = cache.get(id)
    if filtered_talentos is None:
        talentos_list = Talento.objects.order_by('nome')
        filtered_talentos = talentos_list

        if id == 'UXD':
            filtered_talentos = Talento.objects.filter(is_uxdesigner=True)
        elif id == 'UID':
            filtered_talentos = Talento.objects.filter(is_uidesigner=True)
        elif id == 'UXW':
            filtered_talentos = Talento.objects.filter(is_uxwriter=True)
        else:
            filtered_talentos = Talento.objects.order_by('nome')

        cache.set(id, filtered_talentos)
    print(filtered_talentos)
    return render(request, 'filter-talentos.html', {'talentos': filtered_talentos})


def talento_detalhe(request, id):

    obj = get_object_or_404(Talento, pk=id)

    return render(request, 'talento-detalhe.html', {'obj': obj})
