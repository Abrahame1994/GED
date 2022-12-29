from rest_framework import serializers
from App.models import *


class AddUserAppartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appartuser
        fields = ['id_appart']