from django import forms
from .models import Comentario


class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comentario
        fields = ["texto"]
        widgets = {
            "texto": forms.Textarea(attrs={
                "class": "form-control",
                "name": "texto",
                "placeholder": "Leave a comment"
            })
        }
