from django.shortcuts import render
from usuarios.models import Personal

def index(request):

    listado_usuarios = Personal.objects.all()

    return render(request, "usuarios/index.html", {"usuarios":listado_usuarios})
