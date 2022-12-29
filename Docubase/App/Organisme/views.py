from rest_framework.views import APIView
from rest_framework.response import Response
from App.models import Organisme
from .serializers import *
import datetime

class Crud(APIView):

    def generate(self,libelle):
        x = ""
        for i in range(len(libelle)):
            if i< 3:
                x = x + libelle[i]
        return x


    def post(self,request):
        serial = AddOrganismeSerializer(data = request.data)
        print(request.data, serial.is_valid())
        if serial.is_valid():
            organisme = Organisme.objects.create(
                libelle = serial.data['libelle'],
                description = serial.data['description'],
                date_enreg = datetime.date.today()
            )
            
            organisme.code = self.generate(serial.data['libelle']) + str(organisme.id)[0]
            
            org = organisme.save()
            serial = GetOrganismeSerializer(org)

            
            return Response(status = 200, data = serial.data)
        return Response(status = 400)

    
    def get(self,request):
        organismes = Organisme.objects.all()
        serial = GetOrganismeSerializer(organismes,many = True)
        return Response(status = 200, data = serial.data)

    
    def put(self,request):
        
        serial = GetOrganismeSerializer(data = request.data)
        if serial.is_valid():
            organisme = Organisme.objects.get(id = request.query_params.get('id'))
            organisme.libelle = serial.data['libelle']
            organisme.description = serial.data['description']
            organisme.save()
            return Response(status = 200)
        return Response(status = 400)

    def delete(self,request):
        Organisme.objects.get(id = request.query_params.get('id')).delete()
        return Response(status = 200)
        
        