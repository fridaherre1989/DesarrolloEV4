from django.db import models
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    CATEGORIA = models.ForeignKey('CATEGORIA', on_delete=models.PROTECT, null=True, blank=True)

    class CATEGORIA (models.Model):
        nombre = models.CharField (max_length=50)

    def __str__(self):
        return self.nombre

