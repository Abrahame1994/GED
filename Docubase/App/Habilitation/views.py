from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from App.TypeHabilitation.serializers import GetTypeHabilitationSerializer

class Crud(APIView):

    def post(self,request):
        serial = AddHabilitationSerializer(data = request.data)
        if serial.is_valid():
            type_habilitation = TypeHabilitation.objects.get(id = serial.data['type_habilitation'])
            habilitation = Habilitation.objects.create(
                type_habilitation = type_habilitation,
                nom = serial.data['nom'],
                description = serial.data['description']
            )
            data = {
                'habilitation' : GetHabilitationSerializer(habilitation).data,
                'type_habilitation' : GetTypeHabilitationSerializer(type_habilitation).data,
            }
            return Response(status = 200, data = data)
        return Response(status = 400)

    def get(self,request):
        habilitation = Habilitation.objects.all()
        data =  list()
        for i in habilitation:
            data.append(
                {
                'habilitation' : GetHabilitationSerializer(i).data,
                'type_habilitation' : GetTypeHabilitationSerializer(i.type_habilitation).data,
            }
            )
        
        return Response(status = 200, data = data)
    
    def put(self,request):
        serial = GetHabilitationSerializer(data = request.data)
        if serial.is_valid():
            habilitation = Habilitation.objects.get(id = request.query_params.get('id'))
            habilitation.nom = serial.data['nom']
            habilitation.description = serial.data['description']
            habilitation.type_habilitation = TypeHabilitation.objects.get(id = serial.data['type_habilitation'])
            return Response(status = 200)
        return Response(status = 200)

    def delete(self,request):
        Habilitation.objects.get(id = request.query_params.get('id')).delete()
        return Response(status = 200)

class GetByType(APIView):

    def get(self, request):
        type_habilitation = TypeHabilitation.objects.get(id = request.query_params.get('id'))
        habilitation = Habilitation.objects.filter(type_habilitation = type_habilitation.id)
        data = {
                'habilitation' : GetHabilitationSerializer(habilitation,many = True).data,
                'type_habilitation' : GetTypeHabilitationSerializer(type_habilitation).data,
            }
        return Response(status = 200, data = data)