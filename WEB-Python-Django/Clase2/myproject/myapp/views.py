from typing import Sequence
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.

def index (request):

    ctx = {
        "alumnos" : [ "Juan", "Sofi", "Tomi"]
    }

    return render(request, "myapp/index.html", ctx)


def cursos ( request):
    
    conn = sqlite3.connect("db.sqlite3")
    cursor= conn.execute("SELECT nombre, inscriptos FROM cursos")
    cursos = cursor.cursor.fetchall()
    conn.close()
    
    ctx = { "cursos" : cursos}
    return render(request, "myapp/cursos.html", ctx)
