from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SpecieForm
from . import models

# Create your views here.

def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = SpecieForm(request)
        if form.is_valid(): # validation du formulaire.
            Specie = form.save() # sauvegarde dans la base
            return render(request,"affiche.html",{"Specie" : Specie}) # envoie vers une page d'affichage du livre créé
        else:
            return render(request,"ajout.html",{"form": form})
    else:
        form = SpecieForm() # création d'un formulaire vide
        return render(request,"ajout.html",{"form" : form})

def traitement(request):
    lform = SpecieForm(request.POST)
    Specie = lform.save()
    if lform.is_valid():
        return HttpResponseRedirect("/sealife/")
    else:
        return render(request,"sealife/ajout.html",{"form": lform})


def traitementupdate(request, id):
    lform = SpecieForm(request.POST)
    if lform.is_valid():
        Specie = lform.save(commit=False)
        Specie.id = id
        Specie.save()
        return HttpResponseRedirect("/sealife/")
    else:
        return render(request, "sealife/update.html", {"form": lform, "id": id})

def home(request):
    liste = list(models.Animal.objects.all())
    return render(request, 'sealife/home.html', {'liste': liste})

def delete(request, id):
    Animal = models.Animal.objects.get(pk=id)
    Animal.delete()
    return HttpResponseRedirect("/sealife/")


def affiche(request, id):
    specie = models.Animal.indexes.get(pk=id)
    return render(request,"sealife/affiche.html",{"specie" : specie})

def update(request, id):
    specie = models.Animal.objects.get(pk=id)
    lform = SpecieForm(specie.dico())
    return render(request, "sealife/update.html", {"form": lform,"id":id})