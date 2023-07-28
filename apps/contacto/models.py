from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    mensaje = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
