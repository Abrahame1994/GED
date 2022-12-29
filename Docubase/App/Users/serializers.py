from rest_framework import serializers
from App.models import Users

class AddUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['username','password','statuts']



class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class UserLoginSerial(serializers.Serializer):

    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 100)

    
