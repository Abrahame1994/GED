from rest_framework import serializers
from rest_framework.response import Response
from App.models import * 

class AddTypeHabilitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeHabilitation
        fields = ['nom']

class GetTypeHabilitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeHabilitation
        fields = '__all__'