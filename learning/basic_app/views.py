from django.shortcuts import render
from django.http import HttpResponse
from basic_app.forms import *
from basic_app.models import *

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice")

def formpage(request):
    form=forms.formname()

    if request.method=='POST':
        form=forms.formname(request.POST)
        if form.is_valid():
            print("NAME--> "+form.cleaned_data['name'])
            print("TECHNOLOGY--> "+form.cleaned_data['technology'])
            print("EMAIL--> "+form.cleaned_data['email'])
        else:
            print("Invalid form")
    return render(request,'basic_app/formpage.html',{'form':form})

def modelpage(request):
    form=forms.modelname()
    if request.method=='POST':
        form=forms.modelname(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            form=forms.modelname()

    return render(request,'basic_app/modelpage.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print("someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
    else:
        return render(request,'basic_app/login.html',{})



def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def home(request):
    return HttpResponse('<h1>Welcome Sanjay kumar patel and lata ben patel</h1>')