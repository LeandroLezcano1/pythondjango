from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import equipo
from .forms import equipoform, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def about_me(request):
    return render(request, 'paginas/about_me.html')

def equipos(request):
    equipos = equipo.objects.all()
    return render(request, 'equipos/index.html', {'equipos': equipos})

@login_required
def crear(request):
    formulario = equipoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('equipos')
    return render(request, 'equipos/crear.html', {'formulario': formulario})

@login_required
def editar(request, id):
    eq = equipo.objects.get(id=id)
    formulario = equipoform(request.POST or None, request.FILES or None, instance=eq)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('equipos')
    return render(request, 'equipos/editar.html', {'formulario': formulario})

@login_required
def eliminar(request, id):
    eq = equipo.objects.get(id=id)
    eq.delete()
    return redirect('equipos')

def signup(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(request, f'Usuario {username} creado')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'paginas/signup.html', context)