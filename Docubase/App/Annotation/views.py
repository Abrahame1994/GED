from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .serializers import *
from App.models import *
from rest_framework.parsers import MultiPartParser
from App.Apparts.serializers import *
from App.Organisme.serializers import *

class Crud(APIView):

    parsers_class = [MultiPartParser]

    def post(self,request):
        serial = AddAnnotationSerializer(data = request.data)
        if serial.is_valid():
            user = None
            for i in Users.objects.all():
                if check_password(i.username,request.query_params.get('id')):
                    user = i
            courrier = Courrier.objects.get(id = serial.data['courrier'])
            annotation = Annotation.objects.create(
                titre = serial.data['titre'],
                courrier = courrier,
                user = user,
                contenu = request.data['contenu'],
            )

            data = list()
            appart = Appartuser.objects.get(id_user = user).id_appart
            data = { 
                'annotation' : GetAnnotationSerializer(annotation).data,
                'appart': GetAppartSerializer(appart).data,
                'organisme' : GetOrganismeSerializer(appart.organisme).data
            }

            return Response(status = 200, data = data)
        return Response(status = 400)


    def get(self,request):

        annotation = Annotation.objects.filter(courrier = request.query_params.get('id'))
        data = list()
        for i in annotation:
            appart = Appartuser.objects.get(id_user = i.user).id_appart
            data.append({ 
                'annotation' : GetAnnotationSerializer(i).data,
                'appart': GetAppartSerializer(appart).data,
                'organisme' : GetOrganismeSerializer(appart.organisme).data
            })
        
        return Response(status = 200, data = data)


