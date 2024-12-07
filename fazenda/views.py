from django.shortcuts import render, redirect, get_object_or_404
from .models import Proprietario, Animal
from .forms import ProprietarioForm, AnimalForm

# Página inicial
def index(request):
    return render(request, 'fazenda/index.html')

# Listar proprietários
def proprietarios(request):
    proprietarios = Proprietario.objects.all()
    return render(request, 'fazenda/proprietarios.html', {'proprietarios': proprietarios})

# Listar animais
def animais(request):
    animais = Animal.objects.all()
    return render(request, 'fazenda/animais.html', {'animais': animais})

# Adicionar proprietário
def adicionar_proprietario(request):
    if request.method == 'POST':
        form = ProprietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proprietarios')
    else:
        form = ProprietarioForm()
    return render(request, 'fazenda/adicionar_proprietario.html', {'form': form})

# Editar proprietário
def editar_proprietario(request, id):
    proprietario = get_object_or_404(Proprietario, id=id)
    if request.method == 'POST':
        form = ProprietarioForm(request.POST, instance=proprietario)
        if form.is_valid():
            form.save()
            return redirect('proprietarios')
    else:
        form = ProprietarioForm(instance=proprietario)
    return render(request, 'fazenda/editar_proprietario.html', {'form': form, 'proprietario': proprietario})

# Apagar proprietário
def apagar_proprietario(request, id):
    proprietario = get_object_or_404(Proprietario, id=id)
    if request.method == 'POST':
        proprietario.delete()
        return redirect('proprietarios')
    return render(request, 'fazenda/apagar_proprietario.html', {'proprietario': proprietario})

# Adicionar animal
def adicionar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animais')
    else:
        form = AnimalForm()
    return render(request, 'fazenda/adicionar_animal.html', {'form': form})

# Editar animal
def editar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animais')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'fazenda/editar_animal.html', {'form': form, 'animal': animal})

# Apagar animal
def apagar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('animais')
    return render(request, 'fazenda/apagar_animal.html', {'animal': animal})
