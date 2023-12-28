from django.db import models

# Create your models here.


class sexe(models.Model):
    nom = models.CharField(max_length=50)

   



class Donnee(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)
    sexe = models.ForeignKey(sexe, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(null=True)

 
  

class RDV(models.Model):
   
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)
    sexe = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    Heure = models.TimeField(null=True)

