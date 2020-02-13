from django.db import models
from django.utils import timezone


# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=50,null=False)
    delete =  models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estado
    
    class Meta:
        db_table = 'Estado'

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=50,null=False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    delete =  models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ciudad
    
    class Meta:
        db_table = 'Ciudad'

class Genero(models.Model):
    genero = models.CharField(max_length=50,null=False)
    delete =  models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.genero
    
    class Meta:
        db_table = 'Genero'

class Ocupacion(models.Model):
    ocupacion = models.CharField(max_length=50,null=False)
    delete =  models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ocupacion
    
    class Meta:
        db_table = 'Ocupacion'

class Estadocivil(models.Model):
    estadocivil = models.CharField(max_length=50, null=False)
    delete =  models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estadocivil
    
    class Meta:
        db_table = 'Estadocivil'

class Profile(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apPaterno = models.CharField(max_length=50, null=False)
    apMaterno = models.CharField(max_length=50, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(Ocupacion,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    estadocivil = models.ForeignKey(Estadocivil,on_delete=models.CASCADE)
    delete =  models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Profile'



