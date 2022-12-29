from rest_framework import serializers
from App.models import *


class AddTrafficSerializer(serializers.ModelSerializer):

    class Meta:
        model = Traffic
        fields = ['courrier',]


class GetTrafficSerializer(serializers.ModelSerializer):

    class Meta:
        model = Traffic
        fields ='__all__'

class PutTrafficSerializer(serializers.ModelSerializer):

    class Meta:
        model = Traffic
        fields = ['destinataire']