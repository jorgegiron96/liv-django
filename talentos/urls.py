from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.talentos, name = 'talentos'),
    path('talento-detalhe/<int:id>', views.talento_detalhe, name = 'talento-detalhe'),
    # path('admin/', include('admin.site.urls')),
]