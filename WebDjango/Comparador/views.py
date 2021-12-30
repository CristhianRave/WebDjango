import csv
import requests
from django.shortcuts import render
import sqlite3
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.generic.list import ListView

#Modelos
from .models import ModelCards



def home(request):

    return render(request,
                  '../templates/home.html',
                    {'   ',})


def cards(request):

    obj_list = ModelCards.objects.all()  # Todos los objetos de datos
    
    #Paginator
    paginator = Paginator(obj_list, 8)  # cantidad de articulos por pagina
    page = request.GET.get('page')  # Recogemos el parametro 'page'
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

"""     # Definir una instancia de objeto de paginación
    page_obj = Paginator(obj_list, 10)
    pages = page_obj.page(pid)  # Pase el número de páginas al objeto page_obj
    # datos paginados de pages.object_list """
