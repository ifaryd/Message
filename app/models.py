from django.db import models

class Langue(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    initial = models.TextField()
    classe = models.TextField(blank=True, null=True)  # This field type is a guess.
    type_contenu = models.TextField(blank=True, null=True)
    sens_lecture = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.initial
    class Meta:
        db_table = 'langue'

class Predication(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    numero = models.IntegerField(blank=True, null=True)
    nom_pred = models.TextField(blank=True, null=True)  # This field type is a guess.
    titre = models.TextField(blank=True, null=True)
    sous_titre = models.TextField(blank=True, null=True)
    nom_audio = models.TextField(blank=True, null=True)
    lien_audio = models.TextField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    id_langue = models.ForeignKey('Langue', db_column='id_langue', on_delete=models.CASCADE)
    lien_video = models.TextField(blank=True, null= True)
    def __str__(self):
        return self.titre
    class Meta:
        db_table = 'predication'

class Verset(models.Model):  
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    numero = models.IntegerField(blank=True, null=True)
    contenu = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_langue = models.ForeignKey('Langue', db_column='id_langue', on_delete=models.CASCADE)
    id_pred = models.ForeignKey('Predication', db_column='id_pred', on_delete=models.CASCADE)
    #id_parab = models.ForeignKey('Parabole', on_delete=models.CASCADE)
    def __str__(self):
        return self.contenu
    class Meta:
        db_table = 'verset'