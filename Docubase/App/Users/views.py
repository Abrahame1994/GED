from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from App.models import *
from .serializers import *
from App.TypeHabilitation.serializers import GetTypeHabilitationSerializer
from App.Habilitation.serializers import GetHabilitationSerializer
from App.Utilisateur.serializers import *
from App.Apparts.serializers import *
from App.Organisme.serializers import *
# Connecté / Non Connecté
class Login(APIView):

    def post(self,request):
        
        serial = UserLoginSerial(data = request.data)
        print(request.data, serial.is_valid())
        user = None
        if serial.is_valid():
            data = list()
            for i in Users.objects.all():
                if serial.data['username'] == i.username and check_password(serial.data['password'],i.password):
                    user = i
            if user:
                i.statuts = "Connecté"
                i.save()
                    
                token = make_password(password=serial.data['username'],salt = None,hasher="pbkdf2_sha256")
                appart = Apparts.objects.get(id = Appartuser.objects.get(id_user = i.id).id_appart.id)
                h_appart = HabilitationApparts.objects.filter(id_apparts = appart)
                for i in h_appart:
                    data.append(
                                i.id_habilitation.nom
                                #'habilitation' : GetHabilitationSerializer(i.id_habilitation).data
                                #'type_habilitation' : GetTypeHabilitationSerializer(i.id_habilitation.type_habilitation).data,
                            )
                return Response(status = 200, data = {'token': token,
                                                      'habilitation': data,
                                                      'user': GetUtilisateurSerializer(user.user).data,
                                                      'appart': GetAppartSerializer(appart).data,
                                                      'organisme' : GetOrganismeSerializer(appart.organisme).data})
        return Response(status = 400)

class Logout(APIView):

    def post(self,request):
        pass
