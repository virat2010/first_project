from first_app import views
from django.urls import *
from django.conf.urls import *
app_name = 'first_app'
urlpatterns = [
    path(r'^$',views.index,name='index'),
    path(r'^help/',views.help,name='help'),
    path(r'^users/',views.users,name='users'),
    path(r'^form/',views.form,name='form'),
    path(r'^register/', views.register, name='register'),
    path(r'^login/', views.login, name='login'),
]
