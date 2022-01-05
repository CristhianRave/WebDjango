
from urllib import request
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#Models
from django.contrib.auth.models import User
from .models import ModelCards
from .forms import RegisterForm

# -----------------------------------------------------------

def layout(request):


    return render(request,
                  '../templates/layout.html')

# -----------------------------------------------------------

#Vista de pruebas
def home(request):

    return render(request,
                  '../templates/home.html',
                  {'': ''})

# -----------------------------------------------------------

def cards(request):

    obj_list = ModelCards.objects.all()  #Todos los elementos de la tabla ModelCards
    
    #Sistema de paginacion
    paginator = Paginator(obj_list, 12)  # cantidad de articulos por pagina
    page = request.GET.get('page')  # Recogemos el parametro 'page' desde pagination.html
    page_card = paginator.get_page(page)  # Pasamos el numero de la pagina

    return render(request, 
                '../templates/cards.html',
                  {'card': page_card})

# -----------------------------------------------------------

#Vista de pruebas
def pruebas(request):


    return render(request,
                  '../templates/pruebas.html',
                  {'':''})

# -----------------------------------------------------------

def loginUser(request):

    #Si usuario no registrado trata de acceder
    #  a urls registringidas redirigimos a layout
    if request.user.is_authenticated:  
        return redirect('/layout')
    else:
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('/cards')
        else:
            messages.warning(request, 'No Te has identificado')
            return redirect('/pruebas')

# -----------------------------------------------------------


def logoutUser(request):

    logout(request)

    return redirect('layout')




# -----------------------------------------------------------

def suscribeUser(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                messages.success(request, 'Te has registrado!')

                return redirect('/cards')

        return render(request, '../templates/suscribe.html', {
            'title': 'Registro',
            'register_form': register_form,
        })


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


