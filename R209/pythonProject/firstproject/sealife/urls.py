from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('ajout/', views.ajout),
    path('ajoutCategory/',views.ajoutCategory),
    path('category/', views.category),
    path('traitement/', views.traitement),
    path('traitementCategory/', views.traitementCategory),
    path('affiche/<int:id>/',views.affiche),
    path('afficheCategory/<int:id>/',views.afficheCategory),
    path('update/<int:id>/',views.update),
    path('updateCategory/<int:id>/',views.updateCategory),
    path("delete/<int:id>/",views.delete),
    path("deleteCategory/<int:id>",views.deleteCategory),
    path("traitementupdate/<int:id>",views.traitementupdate),
    path("traitementupdateCategory/<int:id>", views.traitementupdateCategory),
]