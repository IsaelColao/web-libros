from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    autores_ids = models.ManyToManyField(Autor, related_name="libros", verbose_name="Autores")
    
    def __str__(self):
        fila = "Titulo: " + self.titulo 
        return fila
    