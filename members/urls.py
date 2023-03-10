from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user,  name='login'),
    path('home', views.home,  name='home'),
    path('register', views.register_view,  name='register'),
    path('logout', views.logout_view),
    path('projeto-detalhe/<int:id>', views.projeto_detalhe, name='projeto-detalhe'),
    path('projeto-register/', views.projeto_register, name='projeto-register'),
    path('projeto-delete/<int:id>', views.projeto_delete, name='projeto-delete')
]
