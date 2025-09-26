from django.contrib import admin
from . import models

admin.site.register(models.Localisation)
admin.site.register(models.Local)
admin.site.register(models.Energie)
admin.site.register(models.DebitEnergie)
admin.site.register(models.Produit)
admin.site.register(models.MatierePremiere)

admin.site.register(models.UtilisationMatierePremiere)
admin.site.register(models.Metier)
admin.site.register(models.RessourceHumaine)
admin.site.register(models.Machine)
