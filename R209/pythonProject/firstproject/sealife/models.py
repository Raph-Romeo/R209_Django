import django.utils.timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def dico(self):
        return {"name": self.name, "description": self.description, "image": self.image}

class Animal(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null="true")
    specie = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    date_discovered = models.DateField(blank=False,default=django.utils.timezone.now())
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
        return {"category": self.category, "specie": self.specie, "date_discovered": self.date_discovered, "size" : self.size, "weight" : self.weight, "lifespan" : self.lifespan , "depth" : self.depth , "locations" : self.locations , "description" : self.description , "image": self.image}
