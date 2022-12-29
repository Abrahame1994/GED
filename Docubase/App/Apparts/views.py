from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from App.Organisme.serializers import GetOrganismeSerializer
from App.Apparts.serializers import *

class Crud(APIView):
    
    def post(self,request):
        print(request.data)
        serial = AddAppartSerializer(data = request.data)
        if serial.is_valid():
            appart = Apparts.objects.create(
                nom = serial.data['nom'],
                description = serial.data['description'],
                organisme = Organisme.objects.get(id = serial.data['organisme']))

            data = {
                'apparts' : GetAppartSerializer(appart).data,
                'organisme_id' : GetOrganismeSerializer(Organisme.objects.get(id = appart.organisme.id)).data
            }
            return Response(status = 200, data = data)

    def get(self,request):

        data = list()
        app = Apparts.objects.all()
        for i in app:
            data.append(
                {
                'apparts' : GetAppartSerializer(i).data,
                'organisme_id' : GetOrganismeSerializer(Organisme.objects.get(id = i.organisme.id)).data
            }
            )

        return Response(status = 200, data = data)

    def put(self,request):
        serial = GetAppartSerializer(data = request.data)
        if serial.is_valid():
            app = Apparts.objects.get(id = request.query_params.get('id') )
            app.nom = serial.data['nom']
            app.description = serial.data['description']
            org = Organisme.objects.get(id = serial.data['organisme'])
            app.organisme = org
            app.save()
            return Response(status = 200)
        return Response(status = 400)

    def delete(self,request):
        Apparts.objects.get(id = request.query_params.get('id')).delete()
        return Response(status = 200)

class GetByUser(APIView):

    def get(self,request):
        print(request.query_params.get('id'))
        data = list()
        ap = Appartuser.objects.filter(id_user = Users.objects.get(user = request.query_params.get('id')).id)
        print(ap)
        for i in ap:
            data.append(
                GetAppartSerializer(i.id_appart).data
            )
        return Response(status = 200, data = {'appart' : data})


