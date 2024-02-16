import requests, sqlite3
from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index ( request ):
    ctx = {
        "alumnos": ["Juan", "Sofia", "Matias"]
    }
    return render(request, "myapp/index.html", ctx)

def cursos (request):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    cursos = cursor.fetchall()
    conn.close()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)

def nuevo_curso(request):
    form = forms.FormularioCurso()     #creamos la instancia de formulario definido en forms.py
    ctx = {"form": form}               #lo agregamos al contexto
    return render(request, "myapp/nuevo_curso.html", ctx) #lo pasamos a la plantilla nuevo_curso.html
    



