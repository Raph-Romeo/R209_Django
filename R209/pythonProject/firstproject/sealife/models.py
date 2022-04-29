from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Animal(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    type = models.CharField(max_length=100)
    specie = models.CharField(max_length=100)
    date_discovered = models.DateField(blank=False)
    size = models.IntegerField(blank=False)
    weight = models.IntegerField(blank=False)
    lifespan = models.IntegerField(blank=False)
    depth = models.IntegerField(blank=False)
    locations = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        name = f"The {self.specie}"
        return name

    def dico(self):
        return {"Category": self.type, "specie": self.specie, "Date discovered": self.date_discovered, "size" : self.size, "weight" : self.weight, "lifespan" : self.lifespan , "depth" : self.depth , "locations" : self.locations , "description" : self.description }


class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)# champs de type text long
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def dico(self):
        return {"type": self.name, "description": self.description}