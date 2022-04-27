from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AnimalForm

from . import  models
# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = AnimalForm(request)
        if form.is_valid():
            specie = form.save()
            return HttpResponseRedirect("/sealife/")
        else:
            return render(request,"ajout.html",{"form": form})
    else :
        form = AnimalForm()
        return render(request,"ajout.html",{"form" : form})

def traitement(request):
    form = AnimalForm(request.POST)
    if form.is_valid():
        specie = form.save()
        return HttpResponseRedirect("/sealife/")
    else:
        return render(request,"sealife/ajout.html",{"form": form})


def home(request):
    specie = list(models.Animal.objects.all())
    return render(request, 'home.html', {'liste': specie})

def affiche(request, id):
    specie = models.Animal.objects.get(pk=id)
    return render(request,"affiche.html",{"specie" : specie})

def delete(request, id):
    livre = models.Animal.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/sealife/")

def update(request, id):
    livre = models.Animal.objects.get(pk=id)
    lform = AnimalForm(livre.dico())
    return render(request, "update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    form = AnimalForm(request.POST)
    if form.is_valid():
        specie = form.save(commit=False)
        specie.id = id
        specie.save()
        return HttpResponseRedirect("/sealife/")
    else:
        return render(request, "update.html", {"form": form, "id": id})
