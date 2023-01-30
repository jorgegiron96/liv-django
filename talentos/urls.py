from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.talentos, name = 'index'),
    # path('', views.index, name = 'index'),
    path('filter-talentos/<str:id>', views.filter_talentos, name = 'filter-talentos'),
    path('talentos/', views.talentos, name = 'talentos'),
    path('talento-detalhe/<int:id>', views.talento_detalhe, name = 'talento-detalhe'),
    # path('admin/', include('admin.site.urls')),
]