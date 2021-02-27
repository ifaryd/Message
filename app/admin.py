# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ActualiteAdmin(admin.ModelAdmin):

    list_display = ('field_id', 'date', 'heure', 'details')
    list_filter = ('date',)


class LangueAdmin(admin.ModelAdmin):

    list_display = (
        'field_id',
        'initial',
        'classe',
        'type_contenu',
        'sens_lecture',
    )
    list_filter = (
        'type_contenu',
        'sens_lecture',
    )


class PredicationAdmin(admin.ModelAdmin):

    list_display = (
        'field_id',
        'numero',
        'nom_pred',
        'titre',
        'duree',
        'id_langue',
    )
    list_filter = ('id_langue',)


class VersetAdmin(admin.ModelAdmin):

    list_display = ('field_id', 'numero','id_langue', 'id_pred')
    list_filter = ('id_langue',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Actualite, ActualiteAdmin)
_register(models.Langue, LangueAdmin)
_register(models.Predication, PredicationAdmin)
_register(models.Verset, VersetAdmin)
