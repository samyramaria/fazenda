from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o painel administrativo
    path('', include('fazenda.urls')),  # Incluir as URLs do app "fazenda"
]
