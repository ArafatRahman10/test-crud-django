from django.contrib import admin
from listings.models import Band, Listing

#Nous insérons ces deux lignes
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre') #Liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) #Nous modifions cette ligne en ajoutant un deuxième argument
admin.site.register(Listing)
