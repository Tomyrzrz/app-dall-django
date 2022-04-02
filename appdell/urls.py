from django.urls import path
from .views import index, galeria, basic, full, sidebar_left, sidebar_right, buscar, Registro, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('basic/', basic, name='basic'),
    path('full/', full, name='full'), 
    path('buscar/', buscar, name='buscar'), 
    path('left/', sidebar_left, name='left'),
    path('right/', sidebar_right, name='right'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/pages/login.html',authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/pages/logout.html'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 