
# Register your models here.
from django.contrib import admin
from webApp.models import Categoria, Orden, Productos

admin.site.register(Categoria)
admin.site.register(Orden)
admin.site.register(Productos)
