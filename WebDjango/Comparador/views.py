
import requests
from django.shortcuts import render
from django.core.paginator import Paginator

#Modelos
from django.contrib.auth.models import User
from .models import ModelCards



def home(request):

    return render(request,
                  '../templates/home.html',
                    {'   ',})


def cards(request):

    obj_list = ModelCards.objects.all()  #Todos los elementos de la tabla ModelCards
    
    #Sistema de paginacion
    paginator = Paginator(obj_list, 8)  # cantidad de articulos por pagina
    page = request.GET.get('page')  # Recogemos el parametro 'page' desde pagination.html
    page_card = paginator.get_page(page)  # Pasamos el numero de la pagina

    return render(request, 
                '../templates/cards.html',
                  {'card': page_card})


def pruebas(request):


    return render(request,
                  '../templates/pruebas.html',
                  {'':''})








""" --------------------------lector de cvs---------------------------------------------- """

""" def cards(request):

    #leer archivo csv
    products = list()
    nombre_archivo = "Comparador/static/img/amazon.csv"
    with open(nombre_archivo, encoding='utf-8', mode='r') as archivo:
        lector = csv.reader(archivo, delimiter=",")
        next(lector, None)
        for fila in lector:
            products.append(fila)

    return render(request, '../templates/cards.html',
                  {"products": products}) """


