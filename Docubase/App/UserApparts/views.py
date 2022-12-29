from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from App.Organisme.serializers import GetOrganismeSerializer
from App.Apparts.serializers import *

class GetByUser(APIView):

    def get(self,request):
        print(request.query_params.get('user'))
        data = list()
        ap = Appartuser.objects.filter(id_user = Users.objects.get(user = request.query_params.get('id')).id)
        print(ap)
        for i in ap:
            data.append(
                GetAppartSerializer(i.id_appart).data
            )
        return Response(status = 200, data = {'appart' : data})


class Update(APIView):

    def post(self,request):
        for i in request.data['appart']:
            Appartuser.objects.create(
                id_appart = Apparts.objects.get(id = i),
                id_user = Users.objects.get(user = request.data['user'])
            )
        
        return Response(status = 200)