from django.conf.urls import url
from first_app import views
from django.urls import re_path

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^help/',views.help,name='help'),
]
