from rest_framework.views import APIView
from rest_framework.response import Response
from App.models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser
from django.contrib.auth.hashers import check_password
from App.Utilisateur.serializers import *
from App.Courrier.serializers import *
from App.Apparts.serializers import *
from App.Traffic.serializers import *
from App.Organisme.serializers import *

class Crud(APIView):
    parsers_class = [MultiPartParser]
    
    def post(self,request):
        print(request.data)
        serial = AddCourrielSerializer(data = request.data)
        
        if serial.is_valid():
            
            user = None
            
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            
            if user:   
                courrier = Courrier.objects.create(
                    contenu = request.data['contenu'],
                    objet = serial.data['objet'],
                    user = user,
                    type = True
                )
                data = {
                    'courrier' : GetCourrielSerializer(courrier).data,
                    'user' : GetUtilisateurSerializer(user.user).data
                }
                serial = GetCourrielSerializer(courrier)
                return Response(status = 200, data = data)
        return Response(status = 400)


    def get(self,request):
            user = None
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            

            appart = Appartuser.objects.get(id_user = user).id_appart
           
            courrier = Courrier.objects.filter(type = True)

            data = list()
            for i in courrier:
                appart_courriel = Appartuser.objects.get(id_user = i.user).id_appart

                if appart_courriel == appart:

                        data.append(
                       {
                            'courrier' : GetCourrielSerializer(i).data,
                            'user' : GetUtilisateurSerializer(i.user.user).data,
                        }
                    )
   
            return Response(status = 200, data = data)

class GetCourrierEnvoye(APIView):

    def get(self,request):

            user = None
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            
            appart = Appartuser.objects.get(id_user = user).id_appart

            courrier = Courrier.objects.filter(statut = True)
            real_courrier = list()
            for i in courrier:
                
                traffic = Traffic.objects.filter(courrier = i)
                for j in traffic:
                    if Appartuser.objects.get(id_user = j.user).id_appart == appart :
                        real_courrier.append({
                        'traffic' : GetTrafficSerializer(j).data,
                        'courrier' : GetCourrielSerializer(j.courrier).data,
                        'destinataire' : GetAppartSerializer(j.destinataire).data,
                        'organisme' : GetOrganismeSerializer(j.destinataire.organisme).data
                    })
            return Response(status = 200, data = real_courrier)

class CourrierRecu(APIView):

    def get(self,request):

            user = None
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            

            appart = Appartuser.objects.get(id_user = user).id_appart


            traffic = Traffic.objects.filter(destinataire = appart)
            data = list()
            for i in traffic:
                appart = Appartuser.objects.get(id_user = i.courrier.user).id_appart
                data.append({
                    'traffic' : GetTrafficSerializer(i).data,
                    'courrier' : GetCourrielSerializer(i.courrier).data,
                    'expediteur' : GetAppartSerializer(appart).data,
                    'organisme' : GetOrganismeSerializer(appart.organisme).data
                })
            return Response(status = 200, data = data)


class Consultation(APIView):

    def put(self,request):
            traffic = Traffic.objects.get(id = request.data['id'])
            traffic.statut = True
            traffic.save()
            return Response(status = 200)

class CourrierSortant(APIView):

    def post(self,request):
        print(request.data)
        serial = AddCourrielSortantSerializer(data = request.data)
        
        if serial.is_valid():
            
            user = None
            
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            print(user)
            if user:   
                courrier = Courrier.objects.create(
                    contenu = request.data['contenu'],
                    objet = serial.data['objet'],
                    categorie = serial.data['categorie'],
                    destination = serial.data['destination'],
                    user = user,
                    type = False
                )
                data = {
                    'courrier' : GetCourrielSerializer(courrier).data,
                    'user' : GetUtilisateurSerializer(user.user).data
                }
                serial = GetCourrielSerializer(courrier)
                return Response(status = 200, data = data)
        return Response(status = 400)

    
    def get(self,request):
            user = None
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            

            appart = Appartuser.objects.get(id_user = user).id_appart
           
            courrier = Courrier.objects.filter(type = False)

            data = list()
            for i in courrier:
                appart_courriel = Appartuser.objects.get(id_user = i.user).id_appart 

                if appart_courriel == appart:

                        data.append(
                       {
                            'courrier' : GetCourrielSerializer(i).data,
                            'user' : GetUtilisateurSerializer(i.user.user).data,
                        }
                    )
   
            return Response(status = 200, data = data)




        



            

