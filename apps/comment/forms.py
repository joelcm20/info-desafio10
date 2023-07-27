from django import forms
from .models import Comentario


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
        widgets = {
            "texto": forms.Textarea(attrs={
                "class": "form-control bg-body-tertiary",
                "name": "texto",
                "placeholder": "Deja un comentario..."
            })
        }
        labels = {
            "texto": "Comentar"
        }
