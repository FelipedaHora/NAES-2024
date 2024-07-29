from django.contrib import admin

# Importe duas classes
from .models import Tarefa, Projeto

# Register your models here.
admin.site.register(Tarefa)
admin.site.register(Projeto)