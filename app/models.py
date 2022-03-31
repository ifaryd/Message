# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from enum import auto
from django.db import models


class Assemblee(models.Model):
    nom = models.TextField(blank=True, null=True)
    situation = models.TextField(blank=True, null=True)
    num_ville = models.TextField(blank=True, null=True)
    num_dirigeant = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assemblee'


class Cantique(models.Model):
    numero = models.TextField(blank=True, null=True)
    titre = models.TextField(blank=True, null=True)
    lien_audio = models.TextField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    num_chantre = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    paroles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantique'


class Chantre(models.Model):
    numero = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chantre'


class Charge(models.Model):
    numero = models.TextField(blank=True, null=True)
    titre = models.TextField(blank=True, null=True)
    id_langue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charge'


class Concordance(models.Model):
    num_pred = models.TextField(blank=True, null=True)
    num_verset = models.TextField(blank=True, null=True)
    concordance = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concordance'


class Confirmes(models.Model):
    numero = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    ref_image = models.TextField(blank=True, null=True)
    sigle_pays = models.TextField(blank=True, null=True)
    lien = models.TextField(blank=True, null=True)
    lien_image = models.TextField(blank=True, null=True)
    page_facebook = models.TextField(blank=True, null=True)
    page_youtube = models.TextField(blank=True, null=True)
    id_langue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confirmes'


class Dirigeant(models.Model):
    numero = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    tel1 = models.TextField(blank=True, null=True)
    tel2 = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    page_facebook = models.TextField(blank=True, null=True)
    page_youtube = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dirigeant'


class Langue(models.Model):
    _id = models.AutoField(primary_key=True)
    initial = models.TextField()
    nom_langue = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.initial

    class Meta:
        managed = False
        db_table = 'langue'


class Livre(models.Model):
    lien_pdf = models.TextField(blank=True, null=True)
    nom_livre = models.TextField(blank=True, null=True)
    extrait_de = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livre'


class Ministre(models.Model):
    numero = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    tel1 = models.TextField(blank=True, null=True)
    tel2 = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    num_charge = models.TextField(blank=True, null=True)
    sigle_pays = models.TextField(blank=True, null=True)
    page_facebook = models.TextField(blank=True, null=True)
    page_youtube = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ministre'


class Pays(models.Model):
    nom = models.TextField(blank=True, null=True)
    sigle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pays'


class Photo(models.Model):
    description = models.TextField(blank=True, null=True)
    lien = models.TextField(blank=True, null=True)
    id_langue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photo'


class Predication(models.Model):
    _id = models.AutoField(primary_key=True)
    numero = models.TextField(blank=True, null=True)
    chapitre = models.TextField(blank=True, null=True)
    titre = models.TextField()
    sous_titre = models.TextField(blank=True, null=True)
    nom_audio = models.TextField(blank=True, null=True)
    lien_audio = models.TextField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    lien_video = models.TextField(blank=True, null=True)
    similar_sermon = models.TextField(blank=True, null=True)
    lien_pdf = models.TextField(blank=True, null=True)
    id_langue = models.ForeignKey('Langue', db_column='id_langue', on_delete=models.CASCADE)
    def __str__(self):
        return self.titre

    class Meta:
        managed = False
        db_table = 'predication'


class Temoignage(models.Model):
    titre = models.TextField(blank=True, null=True)
    texte = models.TextField(blank=True, null=True)
    id_langue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'temoignage'


class Verset(models.Model):
    _id = models.AutoField(primary_key=True)
    numero = models.TextField(blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)
    num_pred = models.ForeignKey('Predication', db_column='num_pred', on_delete=models.CASCADE, related_name="pred_verset")
    info = models.TextField(blank=True, null=True)
    id_langue = models.ForeignKey('Langue', db_column='id_langue', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'verset'


class Video(models.Model):
    titre = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lien = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    id_langue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'video'


class Ville(models.Model):
    numero = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    sigle_pays = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ville'
