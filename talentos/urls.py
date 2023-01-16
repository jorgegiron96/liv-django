from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('talentos/filter-items/<str:id>/', views.filter_talentos, name = 'filter_items'),
    path('talentos/', views.talentos, name = 'talentos'),
    path('talento-detalhe/<int:id>', views.talento_detalhe, name = 'talento-detalhe'),
    # path('admin/', include('admin.site.urls')),
]