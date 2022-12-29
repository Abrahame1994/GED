from rest_framework import serializers
from App.models import *

class AddHabilitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habilitation
        fields = ['nom','description','type_habilitation'] 


class GetHabilitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habilitation
        fields = '__all__' 