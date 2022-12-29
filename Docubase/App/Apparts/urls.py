from django.urls import *
from .views import *

urlpatterns = [
    path('crud/', Crud.as_view())
]