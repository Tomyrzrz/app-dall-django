from django.shortcuts import render, redirect
from .models import Producto, Servicio, Comentarios
from .forms import ComentariosForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView

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



class Registro(View):
  form_class = userForm
  initial = {'key': 'value'}
  template_name = 'app/pages/registro.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs): 
    form = self.form_class(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}')
        return redirect(to='/')
    return render(request, self.template_name, {'form': form})
  def dispatch(self, request, *args, **kwargs):
    # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
        return redirect(to='/')
    # else process dispatch as it otherwise normally would
    return super(Registro, self).dispatch(request, *args, **kwargs)




class CustomLoginView(LoginView):
  form_class = loginForm
  def form_valid(self, form):
    remember_me = form.cleaned_data.get('remember_me')
    if not remember_me:
        # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
        self.request.session.set_expiry(0)
        # Set session as modified to force data updates/cookie to be saved.
        self.request.session.modified = True
    # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
    return super(CustomLoginView, self).form_valid(form)



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

