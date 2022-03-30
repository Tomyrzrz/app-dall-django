from django.contrib import admin
from .models import Servicio, Producto, Comentarios

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display = ["nombre","descripcion_corta","costo"]
  list_editable = ["costo"]
  search_fields = ["nombre","descripcion_corta"]
  list_filter = ["costo"]
  list_per_page = 10

class ServicesAdmin(admin.ModelAdmin):
  list_display = ["nombre","descripcion","costo"]
  search_fields = ["nombre","descripcion"]
  list_per_page = 3

admin.site.register(Producto, ProductAdmin)
admin.site.register(Servicio, ServicesAdmin)
admin.site.register(Comentarios)
