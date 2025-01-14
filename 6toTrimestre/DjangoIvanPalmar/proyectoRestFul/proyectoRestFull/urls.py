"""
URL configuration for proyectoRestFull project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from proyectoRestFull.views import proyectoModuloApis
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',proyectoModuloApis,name='paginaPrincipal'),
    path('usuariosAPI/',include('usuariosAPI.urls')),
    path('habitacionesAPI/',include('habitacionesGestion.urls')),
    path('reservasAPI/', include('reservasAPI.urls')),
    path('APIservicios/', include('APIservicios.urls')),
    path('APIfacturas/', include('APIfacturas.urls')),
    path('documentacion/',include_docs_urls(title='Documentacion de las APis'))
]