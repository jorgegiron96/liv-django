from django.contrib import admin

from .models import Talento, Projeto

class TalentoAdmin(admin.ModelAdmin):
    
    list_display  = ('nome','titulo', 'etapa', 'video', 'is_uxdesigner', 'is_uidesigner', 'is_uxwriter', 'user')


class ProjetoAdmin(admin.ModelAdmin):
    
    list_display  = ('nome','titulo', 'link', 'talento')


admin.site.register(Talento, TalentoAdmin)
admin.site.register(Projeto, ProjetoAdmin)