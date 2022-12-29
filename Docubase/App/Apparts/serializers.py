from rest_framework import serializers
from App.models import *

class AddAppartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apparts
        fields = ['nom','description','organisme']


class GetAppartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apparts
        fields = '__all__'