from django.contrib import admin
from .models import*

# Register your models here.

class sexeAdmin(admin.ModelAdmin):
    list_display=('nom',)



class DonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'sexe','age')


class RDVAdmin(admin.ModelAdmin):
    list_display = ('donnee','Date','Heure')


admin.site.register(sexe,sexeAdmin)
admin.site.register(Donnee,DonneAdmin)
admin.site.register(RDV,RDVAdmin)