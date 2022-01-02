from django.contrib import admin
from .models import ModelCards
# Configuracion extras


class AdminModelCards(admin.ModelAdmin):

    list_display = ['id', 'link','description','price']
    ordering = ('id',)

#Registrar sitios
admin.site.register(ModelCards, AdminModelCards)



# Configuracion del panel de admin
title = 'Web Django'
subtitle = 'Panel de gestion'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
