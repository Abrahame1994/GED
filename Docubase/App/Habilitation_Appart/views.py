from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from App.Habilitation.serializers import *

class Crud(APIView):

    def post(self,request):
        
        serial = AddHabilitationAppart(data = request.data)
        print(request.data,serial.is_valid())
        if serial.is_valid():
            for i in request.data['id_habilitation']:
                    HabilitationApparts.objects.create(
                    id_habilitation = Habilitation.objects.get(id = i),
                    id_apparts = Apparts.objects.get(id = serial.data['id_apparts'])
                )
            return Response(status = 200)
        return Response(status = 400)


    def get(self,request):
        
        appart = Apparts.objects.get(id = request.query_params.get('id'))
        data = list()
        

        for j in HabilitationApparts.objects.all():
            if (appart.id == j.id_apparts.id):
                data.append(j)
        

        datas = list()
        for i in data:

            for j in Habilitation.objects.all():
                if(i.id_habilitation.id == j.id):
                    datas.append(GetHabilitationSerializer(j).data)
        print(datas)
        
        return Response(status = 200, data = datas)

