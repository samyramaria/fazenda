from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proprietarios/', views.proprietarios, name='proprietarios'),
    path('animais/', views.animais, name='animais'),
    path('adicionar_proprietario/', views.adicionar_proprietario, name='adicionar_proprietario'),
    path('adicionar_animal/', views.adicionar_animal, name='adicionar_animal'),
    path('editar_proprietario/<int:id>/', views.editar_proprietario, name='editar_proprietario'),
    path('apagar_proprietario/<int:id>/', views.apagar_proprietario, name='apagar_proprietario'),
    path('editar_animal/<int:id>/', views.editar_animal, name='editar_animal'),
    path('apagar_animal/<int:id>/', views.apagar_animal, name='apagar_animal'),
]
