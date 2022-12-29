"""Docubase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organisme/', include('App.Organisme.urls')),
    path('utilisateur/', include('App.Utilisateur.urls')),
    path('', include('App.Users.urls')),
    path('habilitation/', include('App.Habilitation.urls')),
    path('apparts/', include('App.Apparts.urls')),
    path('habilitationappart/', include('App.Habilitation_Appart.urls')),
    path('typehabilitation/', include('App.TypeHabilitation.urls')),
    path('userapparts/', include('App.UserApparts.urls')),
    path('courrierarrive/', include('App.Courrier.urls')),
    path('traffic/', include('App.Traffic.urls')),
    path('lien/', include('App.Lien.urls')),
    path('courriersortant/',include('App.Courrier.urls')),
    path('annotation/', include('App.Annotation.urls'))
    
]
