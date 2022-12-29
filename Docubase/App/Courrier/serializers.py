from rest_framework import serializers
from App.models import *

class AddCourrielSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courrier
        fields = ['objet','categorie']


class GetCourrielSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courrier
        fields = '__all__'


class PutCourrielSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Courrier
        fields = ['id']


class AddCourrielSortantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Courrier
        fields = ['objet','destination','categorie']