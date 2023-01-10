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
        fields = {'nome', 'titulo','video1', 'video2', 'video3', 'horario_entrev', 'horario_entrev',
                  'semana_entrev','video1_about','video2_about', 'video3_about'}

        widgets = {
            'nome': forms.TextInput(),
            'titulo': forms.TextInput(),
            'video1': forms.TextInput(),
            'video2': forms.TextInput(),
            'video3': forms.TextInput(),
            'horario_entrev': forms.CheckboxSelectMultiple(choices=Projeto.HORARIOS),
            'semana_entrev': forms.CheckboxSelectMultiple(choices=Projeto.DIAS_SEMANA),
            'video1_about': forms.RadioSelect(choices=Projeto.ABOUT_PROJECT_CHOICES),
            'video2_about': forms.RadioSelect(choices=Projeto.ABOUT_PROJECT_CHOICES),
            'video3_about': forms.RadioSelect(choices=Projeto.ABOUT_PROJECT_CHOICES),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['video1'].widget.attrs.update({'class': 'form-control'})
        self.fields['video2'].widget.attrs.update({'class': 'form-control'})
        self.fields['video3'].widget.attrs.update({'class': 'form-control'})
        self.fields['horario_entrev'].widget.attrs.update(
            {'class': 'form-check-input', 'id': "flexCheckDefault"})
        self.fields['semana_entrev'].widget.attrs.update(
            {'class': 'form-check-input', 'id': "flexCheckDefault"})
        self.fields['video1_about'].widget.attrs.update(
            {'class': 'form-check-input',  "id": "flexRadioDefault1"})
        self.fields['video2_about'].widget.attrs.update(
            {'class': 'form-check-input',  "id": "flexRadioDefault2"})
        self.fields['video3_about'].widget.attrs.update(
            {'class': 'form-check-input',  "id": "flexRadioDefault3"})

