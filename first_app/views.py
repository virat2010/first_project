from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
from first_app.forms import FormName,UserForm,UserProfileInfoForm
from . import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('name')
    my_dict = {'insert_me':'Now I am coming from first_app/index.html!','insert_content':"HELLO IM FROM FIRSTAPP!",'access_records':webpages_list}
    return render(request, 'first_app/index.html', context=my_dict)

def help(request):
    my_dict = {'insert_me':"You are at the help page! Don't worry, the error is not for you!"}
    return render(request, 'first_app/help.html', context=my_dict)

def error_404(request, exception):
        data = {}
        return render(request,'first_app/help.html', data)

def register(request):

    registered = True

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile_user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print("Invalid")
            registered = False

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        registered = False
    return render(request, 'first_app/registration.html',context=
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

def login(request):
    return render(request, 'first_app/login.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    my_dict = {'users':user_list}
    return render(request, 'first_app/users.html', context=my_dict)


def form(request):
    form = forms.FormName()
    my_dict = {'form':form,}
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # DO SOMETHING CODE
            form.save(commit=True)
            return users(request)
        else:
            print("Invalid")
    return render(request, 'first_app/form.html', context=my_dict)
