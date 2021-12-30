import csv
import requests
from django.shortcuts import render



def home(request):

    return render(request, '../templates/home.html',
                {"": ""})


def index(request):

    #leer archivo csv
    products = list()
    nombre_archivo = "Comparador/static/img/amazon.csv"
    with open(nombre_archivo, encoding='utf-8', mode='r') as archivo:
        lector = csv.reader(archivo, delimiter=",")
        next(lector, None)
        for fila in lector:
            products.append(fila)

    return render(request, '../templates/index.html',
                  {"products": products})


