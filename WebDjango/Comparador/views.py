import csv
import requests
from django.shortcuts import render
import sqlite3

#Modelos
from .models import modelCards



def home(request):

    return render(request, '../templates/home.html',
                {"": ""})


def cards (request):

    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM amazon")
    usuarios = cursor.fetchall()
    conexion.close()

    return render(request, '../templates/cards.html',
                  {"card": usuarios})


def pruebas(request):

    return render(request, '../templates/pruebas.html',
                  {"": ""})








""" ------------------------------------------------------------------------ """

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
