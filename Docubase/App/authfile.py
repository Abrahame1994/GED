from App.models import Users, Utilisateur
from.django.contrib.auth.hashers import check_password



def authenticate(self,token):
    user = None
    for i in Users.objects.all():
        if check_password(token,i.username):
            user = i
    return {
            'user' : user,
            'utilisateur' : i.user,
        }

def get_habilitation(username):
        user = Users.objects.get(username = username)
        appart = Apparts.objects.filter(id = user.id)
        data = list()
        for i in appart:

            for j in HabilitationApparts:
                if (i.id == j.id_appart.id):
                    data.append(j)

        datas = list()
        for i in data:

            for j in Habilitation.objects.all():
                if(i.id_habilitation == j.id):
                    datas.append(j)
        return datas