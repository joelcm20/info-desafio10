from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe


class NewsAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "title_tag"]

    def image_tag(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='width:50px;height:50px'>")
    image_tag.short_description = "image"

    def title_tag(self, obj):
        return mark_safe(f"<div style='display:flex;align-items:center;height:50px'><h4 style='background-color:green;color:white;display:flex; align-items:center;'>{obj.title}</h4></div>")
    title_tag.short_description = "title"


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category)
