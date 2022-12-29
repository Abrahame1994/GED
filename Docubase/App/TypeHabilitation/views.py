from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class Crud(APIView):

    def post(self,request):
        serial =  GetTypeHabilitationSerializer(data = request.data)
        if serial.is_valid():
            typehabilitation = serial.save()
            serial = GetTypeHabilitationSerializer(typehabilitation)
            return Response(status = 200, data = serial.data)


    def get(self,request):
        type_habilitation =  TypeHabilitation.objects.all()
        serial =  GetTypeHabilitationSerializer(type_habilitation,many = True)
        return Response(status = 200, data = serial.data)

    def put(self,request):
        serial = GetTypeHabilitationSerializer(data = request.data)
        if serial.is_valid():
            t_habilitation = TypeHabilitation.objects.get(id = request.query_params.get('id'))
            t_habilitation.nom = serial.data['nom']
            t_habilitation.save()
            return Response(status = 200)
        return Response(status = 400)

    def delete(self,request):
        TypeHabilitation.objects.get(id = request.query_params.get('id')).delete()
        return Response(status = 400)

