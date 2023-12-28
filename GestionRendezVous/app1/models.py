from django.db import models

class sexe(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Donnee(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)
    sexe = models.ForeignKey(sexe, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.nom


class RDV(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)
    sexe = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    Heure = models.TimeField(null=True)

    def __str__(self):
        return self.nom

