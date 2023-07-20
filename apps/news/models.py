from django.db import models
from django.contrib.auth.models import User
from PIL import Image as Im
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news/")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo si el objeto es nuevo
            # generar un nombre único utilizando UUID
            filename = f"{uuid4().hex}.{self.image.name.split('.')[-1]}"
            self.image.name = filename

        super().save(*args, **kwargs)

        img = Im.open(self.image.path)
        # resize
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

    class Meta:
        verbose_name_plural = "News"
