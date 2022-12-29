# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apparts(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    organisme = models.ForeignKey('Organisme', blank=True, null=True,on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'apparts'


class Appartuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_appart = models.ForeignKey(Apparts, db_column='id_appart', blank=True, null=True,on_delete = models.CASCADE)
    id_user = models.ForeignKey('Users',  db_column='id_user', blank=True, null=True,on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'appartuser'


class Habilitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type_habilitation = models.ForeignKey('TypeHabilitation', db_column='type_habilitation', blank=True, null=True,on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'habilitation'


class HabilitationApparts(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_habilitation = models.ForeignKey(Habilitation,  db_column='id_habilitation', blank=True, null=True,on_delete = models.CASCADE)
    id_apparts = models.ForeignKey(Apparts,  db_column='id_apparts', blank=True, null=True,on_delete = models.CASCADE)
    id_organisme = models.ForeignKey('Organisme',  db_column='id_organisme', blank=True, null=True,on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'habilitation_apparts'


class Organisme(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_enreg = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'organisme'


class TypeHabilitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'type_habilitation'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Utilisateur', blank=True, null=True, on_delete = models.CASCADE)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=1000, blank=True, null=True)
    statuts = models.CharField(max_length=15, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'


class Utilisateur(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=150)
    grade = models.CharField(max_length=100)
    fonction = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dateenreg = models.DateField(db_column='dateEnreg', auto_now_add = True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'utilisateur'

class Courrier(models.Model):
    id = models.BigAutoField(primary_key=True)
    destination = models.CharField(max_length=500, blank=True, null=True)
    categorie = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(auto_now_add = True)
    contenu = models.FileField(upload_to='Document')
    objet = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey('Users', on_delete = models.CASCADE)
    statut = models.BooleanField(default = False)
    type = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'courrier'


class Traffic(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', on_delete = models.CASCADE,null=True, blank=True)
    courrier = models.ForeignKey('Courrier', on_delete = models.CASCADE)
    destinataire = models.ForeignKey('Apparts', on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    statut = models.BooleanField(default = False)

    class Meta:
        managed = True
        db_table = 'traffic'



class Lien(models.Model):

    premier = models.ForeignKey(Apparts, on_delete = models.CASCADE, related_name = 'premier')
    second = models.ForeignKey('Apparts', on_delete = models.CASCADE, related_name = 'second')



class Annotation(models.Model):

    titre = models.CharField(max_length=500)
    user = models.ForeignKey('Users', on_delete = models.CASCADE)
    courrier = models.ForeignKey('Courrier', on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    contenu = models.FileField(upload_to='Annotation')