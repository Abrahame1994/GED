from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', Crud.as_view()),
    path('gethabilitation/', GetByType.as_view())
]