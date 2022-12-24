from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from talentos.models import Talento, Projeto
from django.contrib.auth.decorators import login_required

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

@login_required
def home(request):
    current_user = request.user
    
    obj = get_object_or_404(Talento, user=current_user)
    projetos = Projeto.objects.filter(talento=obj.pk)
    print(projetos)

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
            return render(request,'home.html', {'obj':obj,
            'projetos': projetos})
        else:
            print('Usuário não existe')
    else:
        print('TÁ NO GET')
        return render(request,'home.html', {'obj':obj, 
            'projetos': projetos})

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

@login_required
def projeto_detalhe(request, id):
    talento = get_object_or_404(Talento, user=request.user)
    obj = get_object_or_404(Projeto, pk=id, talento=talento)
    about_choices = [c for c in obj.ABOUT_PROJECT_CHOICES]
    horario_choices = [h for h in obj.HORARIOS]
    semana_choices = [s for s in obj.DIAS_SEMANA]
    dias_da_semana = obj.semana_entrev[:]
    horarios_disponiveis = obj.horario_entrev[:]
    
    if request.method == 'POST':
        semana_entrev = request.POST.getlist('semana_entrev')
        nome = request.POST.get('nome')
        # video1 = request.POST.get('video1')
        # video1_about = request.POST.get('video1_about')
        # video2 = request.POST.get('video2')
        # video2_about = request.POST.get('video2_about')
        # video3 = request.POST.get('video3')
        # video3_about = request.POST.get('video3_about')
        horario_entrev= request.POST.getlist('horario_entrev')
        print(semana_entrev)
        print(nome)
        return redirect('projeto-detalhe',id)
    else:
        return render(request,'projetos/projeto-detalhe.html', {'obj':obj,
        'about_choices':about_choices,
        'horario_choices':horario_choices,
        'semana_choices':semana_choices,
        'dias_da_semana': dias_da_semana,
        'horarios_disponiveis': horarios_disponiveis})

