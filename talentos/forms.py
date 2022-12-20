from django import forms
from talentos.models import Talento

class TalentoEditForm(forms.Form):
    class Meta:
        model = Talento
        fields = "__all__"