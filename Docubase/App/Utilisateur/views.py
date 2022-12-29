from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import datetime
from App.Users.serializers import *
from django.contrib.auth.hashers import make_password
from App.models import *
from App.UserApparts.serializers import *
from App.Apparts.serializers import *
from App.Organisme.serializers import *

class Crud(APIView):

    def post(self,request):
        print(request.data)
        serial = AddUtilisateurSerializer(data = request.data['utilisateur'])
        serial1 = AddUserSerializer(data = request.data['user'])
        serial2 = AddUserAppartsSerializer(data = request.data['userappart'])
        print(serial.is_valid(),serial1.is_valid(),serial2.is_valid())
        if serial.is_valid() and serial1.is_valid():
            utilisateur = Utilisateur.objects.create(
                nom = serial.data['nom'],
                prenom = serial.data['prenom'],
                fonction = serial.data['fonction'],
                adresse = serial.data['adresse'],
                tel = serial.data['tel'],
                email = serial.data['email'],
                dateenreg = datetime.date.today()
            )
            user = Users.objects.create(
                user_id = utilisateur.id,
                username = serial1.data['username'],
                password = make_password(password=serial1.data['password'],salt = None,hasher="pbkdf2_sha256"),
                statuts = "NON"
            )
           
            appart = Apparts.objects.get(id = request.data['userappart']['id_appart'])
            Appartuser.objects.create(
                id_appart = appart,
                id_user = user
                )
            serial = GetUtilisateurSerializer(utilisateur).data
            serial1 = GetUserSerializer(user).data
            serial2 = GetAppartSerializer(appart).data
            serial3 = GetOrganismeSerializer(appart.organisme).data
            data = {'utilisateur': serial, 'user' : serial1, 'appart' : serial2 , 'organisme' : serial3}
            return Response(status = 200, data = data)
        return Response(status = 400)


    def get(self,request):
        data = list()
        user = Users.objects.all()
        print(user)
        for i in user:
            try:
                userapp = Appartuser.objects.get(id_user = i.id)
                appa = Apparts.objects.get(id = userapp.id_appart.id)
                organisme = Organisme.objects.get(id = appa.organisme.id)
                data.append({
                'appart' : GetAppartSerializer(appa).data,
                'user' : '', 
                'utilisateur' : GetUtilisateurSerializer(i.user).data,
                'organisme' :   GetOrganismeSerializer(organisme).data
            })
                
            except:
                data.append({
                'appart' : '',
                'user' : '', 
                'utilisateur' : GetUtilisateurSerializer(i.user).data,
                'organisme' :   ''
            })

        return Response(status = 200,data = data)


        
