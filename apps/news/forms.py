from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "summary", "content", "image", "category_id"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Title", "autofocus": ""}),
            "summary": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Summary"}),
            "content": forms.Textarea(attrs={"class": "form-control mb-3", "placeholder": "Write content"}),
            "image": forms.FileInput(attrs={"class": "form-controls mb-3"}),
            "category_id": forms.Select(attrs={"class": "form-select mb-3"})
        }
        labels = {
            "category_id": "Category"
        }