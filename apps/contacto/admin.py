from django.contrib import admin
from .models import Contacto

class AdminContacto(admin.ModelAdmin):
    list_display = ["nombre", "email", "mensaje"]
    readonly_fields = ["created_at"]

# Register your models here.
admin.site.register(Contacto, AdminContacto)