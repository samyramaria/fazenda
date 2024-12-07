from django.contrib import admin
from .models import Proprietario, Animal

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'tipo', 'proprietario')
