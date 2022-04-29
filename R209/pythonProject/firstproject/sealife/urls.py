from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)