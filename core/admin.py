from django.contrib import admin

from .models import Pais
from .models import Departamento
from .models import Provincia

admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Provincia)
