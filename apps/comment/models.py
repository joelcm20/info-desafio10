from django.db import models
from apps.usuario.models import Usuario
from apps.recetas.models import Receta

# Create your models here.
class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto