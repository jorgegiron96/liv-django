from django import forms
from django.contrib.auth.models import User
from talentos.models import Projeto

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ProjetoCreateForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"