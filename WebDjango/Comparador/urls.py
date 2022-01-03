from django.urls import path, include
from Comparador import views


urlpatterns = [
    path("", views.layout, name="layout"),
    path("home", views.home, name="home"),
    path("cards/", views.cards, name="cards"),
    path("pruebas/", views.pruebas, name="pruebas"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("suscribe/", views.suscribeUser, name="suscribeUser"),
]
