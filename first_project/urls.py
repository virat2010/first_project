"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import *
from first_app import views
from django.urls import *

handler404 = 'first_app.views.error_404'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/', views.help, name='help'),
    url(r'^users/', views.users, name='users'),
    url(r'^form/', views.form, name='form'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'first_app/',include('first_app.urls')),
    url(r'^admin/', admin.site.urls),
]
