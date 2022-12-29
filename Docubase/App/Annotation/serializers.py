from rest_framework import serializers
from App.models import *

class AddAnnotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annotation
        fields = ['titre','courrier']


class GetAnnotationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Annotation
        fields = '__all__'