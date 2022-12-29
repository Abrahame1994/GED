from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from App.models import *
from App.Courrier.serializers import *
from App.Utilisateur.serializers import *
from django.contrib.auth.hashers import check_password

class Crud(APIView):
    def post(self,request):
        print(request.data)
        serial = AddTrafficSerializer(data = request.data)
        
        if serial.is_valid():
            
            user = None
            for i in Users.objects.all():
                if check_password(i.username,request.data['id']):
                    user = i

            courrier = Courrier.objects.get(id = serial.data['courrier'])
            courrier.statut = True
            
            destinataire = Apparts.objects.get(id = request.data['destinataire'])
            Traffic.objects.create(
                courrier = courrier,
                destinataire = destinataire,
                user = user
            )
            courrier.save()
            return Response(status = 200)
            
        return Response(status = 400)


    def put(self,request):
        serial = PutTrafficSerializer(data = request.data)
        if serial.is_valid():
            traffic = Traffic.objects.get(id = request.query_params.get('id'))
            destinataire = Apparts.objects.get(id = serial.data['destinataire'])
            traffic.destinataire = destinataire
            traffic.save()
            return Response(status = 200)
        return Response(status = 400)

    def get(self,request):

        user = None
        for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
        
        courriel = Courrier.objects.filter(user = user)
        real_courrier = []

        for i in courriel:
            traffic = Traffic.objects.filter(courrier = i)
            for j in traffic:
                real_courrier.append({
                    'traffic' : GetTrafficSerializer(j).data,
                    'courrier' : GetCourrielSerializer(j.courrier).data,
                    'destinataire' : GetUtilisateurSerializer(j.destinataire.user).data,
                })

        return Response(status = 200, data = real_courrier)
    
