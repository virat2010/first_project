from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('name')
    user_list = User.objects.order_by('first_name')
    my_dict = {'insert_me':'Now I am coming from first_app/index.html!','insert_content':"HELLO IM FROM FIRSTAPP!",'access_records':webpages_list,'users':user_list}
    return render(request, 'first_app/index.html', context=my_dict)

def help(request):
    my_dict = {'insert_me':'You are at the help page!'}
    return render(request, 'first_app/help.html', context=my_dict)

def error_404(request, exception):
        data = {}
        return render(request,'first_app/help.html', data)
