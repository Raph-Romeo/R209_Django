from django.shortcuts import render

# Create your views here.
def bonjour(request):
    nom = request.GET["nom"]
    prenom = request.GET["prenom"]
    nom = nom + " " + prenom
    return render(request, "bonjour.html", {"nom":nom})

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

from .forms import LivreForm
from . import models

def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"affiche.html",{"livre" : livre}) # envoie vers une page d'affichage du livre créé
        else:
            return render(request,"ajout.html",{"form": form})
    else:
        form = LivreForm() # création d'un formulaire vide
        return render(request,"ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request, "affiche.html", {"livre": livre})
    else:
        return render(request, "ajout.html", {"form": lform})

def affiche(request, id):
    livre = models.Livre.objectq.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"affiche.html",{"livre": livre})

def update(request):
    return render(request,"update.html")
