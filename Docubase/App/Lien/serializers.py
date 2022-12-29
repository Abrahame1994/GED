from rest_framework import serializers
from App.models import *

class AddLienSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lien
        fields = ['premier']