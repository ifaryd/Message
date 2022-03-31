# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


# class ActualiteAdmin(admin.ModelAdmin):

#     list_display = ('field_id', 'date', 'heure')
#     list_filter = ('date',)
#     ordering = ['field_id']
#     list_display_links = ['date']


class LangueAdmin(admin.ModelAdmin):

    list_display = (
        '_id',
        'initial',
        'nom_langue',
        
    )
    ordering = ['_id']
    list_filter = (
        'initial',
    )


class PredicationAdmin(admin.ModelAdmin):

    list_display = ('numero','chapitre','titre','duree','id_langue',)
    ordering = ['_id']
    list_filter = ('id_langue',)
    search_fields = ['numero','chapitre','id_langue',]
    list_display_links = ['chapitre', 'titre',]
    


class VersetAdmin(admin.ModelAdmin):

    list_display = ('numero','id_langue', 'num_pred')
    list_filter = ['id_langue']
    ordering = ['numero']
    list_per_page = 100
    search_fields = ['numero','id_langue__nom_langue',"num_pred__titre"]
    list_display_links = ['numero', 'numero',]



def _register(model, admin_class):
    admin.site.register(model, admin_class)


# _register(models.Actualite, ActualiteAdmin)
_register(models.Langue, LangueAdmin)   
_register(models.Predication, PredicationAdmin)
_register(models.Verset, VersetAdmin)
