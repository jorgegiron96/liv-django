from django.shortcuts import render, get_object_or_404, redirect
from .models import Talento
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
import json


def index(request):

    return redirect('talentos')

def talentos(request):

    talentos_list = Talento.objects.order_by('nome')

    return render(request, 'talentos.html',
                  {'talentos': talentos_list
                   })

def filter_talentos(request, id):
    
    if request.method == 'POST':

        talentos_list = Talento.objects.all()
        if id == 'UXD':
            talentos_list = Talento.objects.filter(is_uxdesigner=True)
        elif id == 'UID':
            talentos_list = Talento.objects.filter(is_uidesigner=True)
        elif id == 'UXW':
            talentos_list = Talento.objects.filter(is_uxwriter=True)

        return render(request, 'filter-items.html',
                    {'talentos': talentos_list
                    })

def talento_detalhe(request, id):

    obj = get_object_or_404(Talento, pk=id)

    return render(request, 'talento-detalhe.html', {'obj': obj})
