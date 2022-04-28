from django.db import models

# Create your models here.

class Animal(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    type = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    specie = models.CharField(max_length = 100)
    date_discovered = models.DateField(blank=False) # champs de type date, pouvant être null ou ne pas être rempli
    size = models.IntegerField(blank=False) # champs de type entier devant être obligatoirement rempli
    weight = models.IntegerField(blank=False)  # champs de type entier devant être obligatoirement rempli
    lifespan = models.IntegerField(blank=False) # champs de type entier devant être obligatoirement rempli
    depth = models.IntegerField(blank=False)
    locations = models.TextField(null = True, blank = True) # champs de type text long
    description = models.TextField(null = True, blank = True) # champs de type text long

    def __str__(self):
        name = f"{self.type} | {self.specie} discovered in {self.date_discovered}"
        return name

    def dico(self):
        return {"type": self.type, "specie": self.specie, "Date discovered": self.date_discovered, "size" : self.size, "weight" : self.weight, "lifespan" : self.lifespan , "depth" : self.depth , "locations" : self.locations , "description" : self.description }