from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from App.models import *
from App.Apparts.serializers import *
from App.Organisme.serializers import *
from django.contrib.auth.hashers import check_password

class Crud(APIView):

    def post(self,request):

        serial = AddLienSerializers(data = request.data)
        if serial.is_valid():
            for i in request.data['amis']:
                premier = Apparts.objects.get(id = i)
                second = Apparts.objects.get(id = serial.data['premier'])
                Lien.objects.create(
                premier = premier,
                second = second
            )
            return Response(status = 200)
        return Response(status = 400)


class LienNonAssocie(APIView):
    
    def addlist(self,liste, liste2):
        data = list()
        for i in liste:
            test = False
            for j in data:
                if i.second == j :
                    test = True
            if test == False:
                data.append(i.second)

        for i in liste2:
            test = False
            for j in data:
                if i.premier == j:
                    test = True
            if test ==  False:
                data.append(i.premier)

        return data


    def get(self,request):

            

            #appart = Appartuser.objects.get(id_user = request.query_params.get('id')).id_appart
            appart = Apparts.objects.get(id = request.query_params.get('id'))
            liste1 = Lien.objects.filter(premier = appart.id)
            liste2 = Lien.objects.filter(second = appart.id)
            data = self.addlist(liste1,liste2)
            print('function result',data)
            

            real_data = list()

            for i in Apparts.objects.all():
                test = False
                for j in data:
                    
                    if i == j:
                        test = True
                if test == False and i != appart:
                    real_data.append(i)

            

            real = list()
            for i in real_data:
                real.append({
                    'appart' : GetAppartSerializer(i).data,
                    'organisme' : GetOrganismeSerializer(i.organisme).data
                })

            
            return Response(status = 200, data = real)
        

class LienAssocie(APIView):

    def addlist(self,liste, liste2):
        data = list()
        for i in liste:
            test = False
            for j in data:
                if i.second == j :
                    test = True
            if test == False:
                data.append(i.second)

        for i in liste2:
            test = False
            for j in data:
                if i.premier == j:
                    test = True
            if test ==  False:
                data.append(i.premier)

        return data


    def get(self,request):

        user = None
        for i in Users.objects.all():
            if check_password(i.username,request.query_params.get('id')):
                user = i
        
        if user:
            appart = Appartuser.objects.get(id_user = user).id_appart
            liste1 = Lien.objects.filter(premier = appart.id)
            liste2 = Lien.objects.filter(second = appart.id)
            print(liste1, liste2)
            data = self.addlist(liste1,liste2)
            print('data', data)
            real = list()
            for i in data:
                if i != appart:
                    real.append({
                        'appart' : GetAppartSerializer(i).data,
                        'organisme' : GetOrganismeSerializer(i.organisme).data
                    })

            return Response(status = 200, data = real)
        return Response(status = 400)