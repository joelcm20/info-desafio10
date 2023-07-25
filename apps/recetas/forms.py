from django import forms
from .models import Receta


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ["nombre", "ingredientes", "imagen", "id_categoria"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder":"Nombre de la receta"}),
            "ingredientes": forms.Textarea(attrs={"class": "form-control mb-3", "placeholder": "Escribir ingredientes"}),
            "imagen": forms.FileInput(attrs={"class": "form-control mb-3"}),
            "id_categoria": forms.Select(attrs={"class": "form-select mb-3"})
        }
        labels = {
            "id_categoria": "categoria"
        }
