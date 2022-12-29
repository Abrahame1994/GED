from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', Crud.as_view()),
    path('getappart/', LienNonAssocie.as_view()),
    path('getappartassocie/',LienAssocie.as_view())
]