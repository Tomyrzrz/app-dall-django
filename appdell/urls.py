from django.urls import path
from .views import index, galeria, basic, full, sidebar_left, sidebar_right, buscar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('basic/', basic, name='basic'),
    path('full/', full, name='full'), 
    path('buscar/', buscar, name='buscar'), 
    path('left/', sidebar_left, name='left'),
    path('right/', sidebar_right, name='right'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 