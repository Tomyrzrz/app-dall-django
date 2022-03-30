from django.shortcuts import render
from .models import Producto, Servicio, Comentarios
from .forms import ComentariosForm

# Create your views here.
def index(request):
  productos = Producto.objects.all()
  servicios = Servicio.objects.all()
  datos = {
    "productos" : productos,
    "servicios": servicios
  }
  return render(request, 'app/index.html', datos)


def galeria(request):
  productos = Producto.objects.all()
  datos = {
    "productos" : productos
  }
  return render(request, 'app/pages/gallery.html', datos)

def basic(request):
  return render(request, 'app/pages/basic-grid.html')

def full(request):
  comentarios = Comentarios.objects.all()
  datos = {
    "form": ComentariosForm,
    "comments": comentarios
  }
  if request.method == 'POST':
    formulario = ComentariosForm(data=request.POST)
    if formulario.is_valid():
      formulario.save() 
    else:
      datos["form"] = formulario
  return render(request, 'app/pages/full-width.html', datos)

def sidebar_left(request):
  return render(request, 'app/pages/sidebar-left.html')
def sidebar_right(request):
  return render(request, 'app/pages/sidebar-right.html')








def buscar(request):
  if request.GET['busqueda']:
    query = request.GET['busqueda']
    productos = Producto.objects.filter(nombre__icontains=query).order_by('-costo')
    datos = {
      "productos" : productos,
      "query": query
    }
    return render(request, 'app/pages/b_.html', datos)
  else:
    return render(request, 'app/pages/b_.html')

