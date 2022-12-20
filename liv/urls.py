from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('talentos.urls')),
    path('talentos/', include('talentos.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'))
   
]
