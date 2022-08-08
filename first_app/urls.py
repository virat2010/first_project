from first_app import views
from django.urls import *
from django.conf.urls import *
app_name = 'first_app'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^help/',views.help,name='help'),
    re_path(r'^users/',views.users,name='users'),
    re_path(r'^form/',views.form,name='form'),
    re_path(r'^register/', views.register, name='register'),
    re_path(r'^login/', views.login, name='login'),
]
