from django.shortcuts import render, get_object_or_404
from .models import Talento
from django.contrib.auth.models import User

def talentos(request):

    talentos_list = Talento.objects.order_by('nome')
    uxd = Talento.objects.filter(is_uxdesigner=1)
    uid = Talento.objects.filter(is_uidesigner=1)
    uxw = Talento.objects.filter(is_uxwriter=1)

    return render(request,'talentos.html', 
    {'talentos': talentos_list,
    'uxd': uxd,
    'uid':uid,
    'uxw':uxw
    })

def talento_detalhe(request, id):
    
    obj = get_object_or_404(Talento, pk=id)
    
    return render(request,'perfil.html', {'obj':obj})



