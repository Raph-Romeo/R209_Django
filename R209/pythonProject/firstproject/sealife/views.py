from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AnimalForm
from .forms import CategoryForm

from . import models
# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = AnimalForm(request)
        if form.is_valid():
            specie = form.save()
            return HttpResponseRedirect("/sealife/search")
        else:
            return render(request,"ajout.html",{"form": form})
    else:
        form = AnimalForm()
        return render(request,"ajout.html",{"form" : form, "count": models.Categories.objects.all().count()})

def traitement(request):
    form = AnimalForm(request.POST,request.FILES)
    if form.is_valid():
        specie = form.save()
        return HttpResponseRedirect("/sealife/search")
    else:
        return render(request,"ajout.html",{"form": form})

def ajoutCategory(request):
    if request.method == "POST":
        form = CategoryForm(request,request.FILES)
        if form.is_valid():
            category = form.save()
            return HttpResponseRedirect("/sealife/search")
        else:
            return render(request,"ajoutCategory.html",{"form": form})
    else :
        form = CategoryForm()
        return render(request,"ajoutCategory.html",{"form" : form})


def traitementCategory(request):
    form = CategoryForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/sealife/search")
    else:
        return render(request,"ajoutCategory.html",{"form": form})


def home(request):
    animals = list(models.Categories.objects.all())
    animal_count = models.Categories.objects.all().count()
    return render(request, 'home.html', {'liste': animals,'count':animal_count})

def category(request):
    species = list(models.Animal.objects.all())
    return render(request,"category.html",{'liste': species})

def affiche(request, id):
    species = models.Animal.objects.get(pk=id)
    species_list = list(models.Animal.objects.filter(category=models.Animal.objects.get(pk=id).category))
    count = models.Animal.objects.filter(category=models.Animal.objects.get(pk=id).category).count()
    return render(request,"affiche.html",{"species" : species,"liste": species_list,"count": count})

def search(request):
    species = models.Categories.objects.all()
    animal_count = models.Categories.objects.all().count()
    return render(request,"search.html",{"liste" : species,"count":animal_count})

def afficheCategory(request, id):
    animal = models.Categories.objects.get(pk=id)
    species = list(models.Animal.objects.filter(category=models.Categories.objects.get(pk=id)))
    return render(request,"category.html",{'liste': species,'animal': animal})

def delete(request, id):
    specie = models.Animal.objects.get(pk=id)
    specie.delete()
    return HttpResponseRedirect("/sealife/search")

def deleteCategory(request, id):
    Category = models.Categories.objects.get(pk=id)
    Species = models.Animal.objects.filter(category=models.Categories.objects.get(pk=id))
    Category.delete()
    Species.delete()
    return HttpResponseRedirect("/sealife/search")

def update(request, id):
    Species = models.Animal.objects.get(pk=id)
    form = AnimalForm(Species.dico())
    return render(request, "update.html", {"form": form,"id":id})

def updateCategory(request, id):
    Category = models.Categories.objects.get(pk=id)
    form = CategoryForm(Category.dico())
    return render(request, "updateCategory.html", {"form": form,"id":id})

def traitementupdate(request, id):
    form = AnimalForm(request.POST,request.FILES)
    if form.is_valid():
        species = form.save(commit=False)
        species.id = id
        species.save()
        return HttpResponseRedirect("/sealife/search")
    else:
        return render(request, "update.html", {"form": form, "id": id})

def traitementupdateCategory(request, id):
    form = CategoryForm(request.POST,request.FILES)
    if form.is_valid():
        species = form.save(commit=False)
        species.id = id
        species.save()
        return HttpResponseRedirect("/sealife/search")
    else:
        return render(request, "update.html", {"form": form, "id": id})