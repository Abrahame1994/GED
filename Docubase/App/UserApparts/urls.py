from django.urls import path
from .views import *

urlpatterns = [
    path('getuserappart/', GetByUser.as_view()),
    path('adduserappart/',Update.as_view()),
]