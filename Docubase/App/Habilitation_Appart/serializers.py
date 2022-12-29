from rest_framework.views import APIView
from rest_framework.response import Response
from App.models import *
from rest_framework import serializers

class AddHabilitationAppart(serializers.ModelSerializer):

    class Meta:
        model = HabilitationApparts
        fields = ['id_apparts']