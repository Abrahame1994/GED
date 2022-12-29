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
    organisme = models.ForeignKey('Organisme', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apparts'


class Appartuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_appart = models.ForeignKey(Apparts, models.DO_NOTHING, db_column='id_appart', blank=True, null=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appartuser'


class Habilitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type_habilitation = models.ForeignKey('TypeHabilitation', models.DO_NOTHING, db_column='type_habilitation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habilitation'


class HabilitationApparts(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_habilitation = models.ForeignKey(Habilitation, models.DO_NOTHING, db_column='id_habilitation', blank=True, null=True)
    id_apparts = models.ForeignKey(Apparts, models.DO_NOTHING, db_column='id_apparts', blank=True, null=True)
    id_organisme = models.ForeignKey('Organisme', models.DO_NOTHING, db_column='id_organisme', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habilitation_apparts'


class Organisme(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_enreg = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organisme'


class TypeHabilitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_habilitation'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Utilisateur', models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=1000, blank=True, null=True)
    statuts = models.CharField(max_length=15, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
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
    dateenreg = models.DateField(db_column='dateEnreg')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilisateur'
