from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Nombre"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3", "placeholder": "Email"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control mb-3", "placeholder": "Escribir mensaje"})
        }
