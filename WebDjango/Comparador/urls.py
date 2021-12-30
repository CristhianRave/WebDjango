from django.urls import path, include
from Comparador import views


urlpatterns = [
    path("", views.home, name="home"),
    path("cards/", views.cards, name="cards"),
    path("pruebas/", views.pruebas, name="pruebas"),

]
