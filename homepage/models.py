from django.db import models

# Create your models here.

#class curso(models.Model):
#    nombre = models.CharField(max_length=10)
#   creditos = models.IntegerField()


class Curso(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    creditos = models.IntegerField()


    def __str__(self):
        return self.id,self.nombre,self.creditos

class foto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    creditos = models.IntegerField()
    foto = models.ImageField(upload_to= "media", null=True)