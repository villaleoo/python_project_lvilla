from django.db import models

# Create your models here.

class User(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    contrasenia=models.CharField(max_length=12)
    
    def __str__(self):
        return f'{self.email}'
        
   
class Article(models.Model):
    titulo=models.TextField()
    contenido=models.TextField()