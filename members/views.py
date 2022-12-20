from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from talentos.models import Talento
from members.forms import UserEditForm

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('funciona')
            login(request, user)
            return redirect('home')

        else:
            messages.warning(request, "Ocorreu um erro ao realizar o login, tente novamente.")
            return redirect('login')

    else:
        print('não logou')
        return render(request, 'login.html')


def home(request):
    current_user = request.user
    
    obj = get_object_or_404(Talento, user=current_user)
    form = UserEditForm(instance =current_user)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        etapa = request.POST['etapa']
        video = request.POST['video']
        ux_design = request.POST.get('ux_design', False)
        ui_design = request.POST.get('ui_design', False)
        ux_writer = request.POST.get('ux_writer', False)
        user = User.objects.filter(username=current_user)
        talento =Talento.objects.filter(user=current_user)
        if user.exists():
            messages.success(request, 'Perfil atualizado')
            user.update(first_name = first_name,
                        last_name= last_name)
            talento.update(
                        etapa= etapa,
                        video= video,
                        is_uxdesigner = ux_design,
                        is_uidesigner = ui_design,
                        is_uxwriter = ux_writer
                        )     
            obj = get_object_or_404(Talento, user=current_user)             
            return render(request,'home.html', {'obj':obj})
        else:
            print('Usuário não existe')
    else:
        print('TÁ NO GET')
        form = UserEditForm(instance =current_user)
        return render(request,'home.html', {'obj':obj,
        'form':form})

def register_view(request):

    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = {username,password1,password2}
        user = User.objects.filter(username=username).first()
        if password1 != password2:
            return render(request, 'register.html',{'form': form})
    
            # return HttpResponse('As duas senhas inseridas não são iguais.')
        elif user:
            return HttpResponse('Já existe um usuário com esse username')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            return render(request, 'register.html',{'form': form})
    

def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def projeto(request):

    return render(request,'projetos/projeto.html')