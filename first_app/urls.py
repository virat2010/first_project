from django.conf.urls import url
from first_app import views
from django.urls import *
from django.conf.urls import *
app_name = 'first_app'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^users/',views.users,name='users'),
    url(r'^form/',views.form,name='form'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
]
