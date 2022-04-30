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
    else :
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
    specie = list(models.Animal.objects.all())
    return render(request,"category.html",{'liste': specie})

def affiche(request, id):
    specie = models.Animal.objects.get(pk=id)
    return render(request,"affiche.html",{"specie" : specie})

def search(request):
    specie = models.Categories.objects.all()
    animal_count = models.Categories.objects.all().count()
    return render(request,"search.html",{"liste" : specie,"count":animal_count})

def afficheCategory(request, id):
    animal = models.Categories.objects.get(pk=id)
    specie = list(models.Animal.objects.filter(category=models.Categories.objects.get(pk=id)))
    return render(request,"category.html",{'liste': specie,'animal': animal})

def delete(request, id):
    specie = models.Animal.objects.get(pk=id)
    specie.delete()
    return HttpResponseRedirect("/sealife/search")

def deleteCategory(request, id):
    Category = models.Categories.objects.get(pk=id)
    Category.delete()
    return HttpResponseRedirect("/sealife/search")

def update(request, id):
    Specie = models.Animal.objects.get(pk=id)
    form = AnimalForm(Specie.dico())
    return render(request, "update.html", {"form": form,"id":id})

def updateCategory(request, id):
    Category = models.Categories.objects.get(pk=id)
    form = CategoryForm(Category.dico())
    return render(request, "updateCategory.html", {"form": form,"id":id})

def traitementupdate(request, id):
    form = AnimalForm(request.POST,request.FILES)
    if form.is_valid():
        specie = form.save(commit=False)
        specie.id = id
        specie.save()
        return HttpResponseRedirect("/sealife/search")
    else:
        return render(request, "update.html", {"form": form, "id": id})

def traitementupdateCategory(request, id):
    form = CategoryForm(request.POST,request.FILES)
    if form.is_valid():
        specie = form.save(commit=False)
        specie.id = id
        specie.save()
        return HttpResponseRedirect("/sealife/search")
    else:
        return render(request, "update.html", {"form": form, "id": id})