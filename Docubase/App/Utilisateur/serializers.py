from rest_framework import serializers
from App.models import Utilisateur

class AddUtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = ['nom','prenom','fonction','adresse','tel','email']

class GetUtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = '__all__'