from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', Crud.as_view()),
    path('envoye/', GetCourrierEnvoye.as_view()),
    path('recu/', CourrierRecu.as_view()),
    path('consultation/', Consultation.as_view()),
    path('add/',CourrierSortant.as_view()),
]