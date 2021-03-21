# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ActualiteAdmin(admin.ModelAdmin):

    list_display = ('field_id', 'date', 'heure')
    list_filter = ('date',)
    ordering = ['field_id']
    list_display_links = ['date']


class LangueAdmin(admin.ModelAdmin):

    list_display = (
        'field_id',
        'initial',
        'classe',
        'type_contenu',
        'sens_lecture',
    )
    ordering = ['field_id']
    list_filter = (
        'type_contenu',
        'sens_lecture',
    )


class PredicationAdmin(admin.ModelAdmin):

    list_display = ('numero','nom_pred','titre','duree','id_langue',)
    ordering = ['field_id']
    list_filter = ('id_langue',)
    search_fields = ['numero','nom_pred','id_langue',]
    list_display_links = ['nom_pred', 'titre',]
    


class VersetAdmin(admin.ModelAdmin):

    list_display = ('numero','id_langue', 'id_pred')
    list_filter = ['id_langue']
    ordering = ['field_id']
    list_per_page = 100
    search_fields = ['numero','id_langue',]
    list_display_links = ['numero', 'id_pred',]



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Actualite, ActualiteAdmin)
_register(models.Langue, LangueAdmin)   
_register(models.Predication, PredicationAdmin)
_register(models.Verset, VersetAdmin)
