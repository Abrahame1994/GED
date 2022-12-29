from rest_framework import serializers
from App.models import Organisme

class AddOrganismeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisme
        fields = ['libelle','description']


class GetOrganismeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisme
        fields = '__all__'

