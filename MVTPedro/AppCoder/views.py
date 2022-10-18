from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.

def curso(request, nombre, apellidos, telefono, fecha_nac):
    curso = Curso(nombre=nombre, apellidos=apellidos, telefono=telefono, fecha_nac=fecha_nac)
    curso.save()
    
    return HttpResponse(f""" <p>Familiar: {curso.nombre} {curso.apellidos} agregado</p> """)
    
def listar(request):
        lista = Curso.objects.all()
        
        return render(request, "listar_familiares.html", {"lista_familiares": lista})