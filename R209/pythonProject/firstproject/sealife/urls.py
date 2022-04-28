from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('ajout/', views.ajout),
    path('category/', views.category),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update),
    path("delete/<int:id>",views.delete),
    path("traitementupdate/<int:id>",views.traitementupdate),
]