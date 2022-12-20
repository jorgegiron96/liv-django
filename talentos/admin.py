from django.contrib import admin

from .models import Talento

class TalentoAdmin(admin.ModelAdmin):
    
    list_display  = ('nome','titulo', 'etapa', 'video', 'is_uxdesigner', 'is_uidesigner', 'is_uxwriter', 'user')


admin.site.register(Talento, TalentoAdmin)
