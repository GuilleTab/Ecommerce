from django.shortcuts import render
from articulos.models import Articulo

def index(request):

    listado_articulos = Articulo.objects.all()

    return render(request, "articulos/index.html", {"articulos":listado_articulos})
