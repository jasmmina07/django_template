from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from random import randrange

# Create your views here.

def main(request):
    data={}
    return render(request,"index.html",data)

def question():
    a=randrange(1,100_000)
    b=bin(a)
    return a,b


def home(request):
    a,b=question
    data={
        "questions":{
            "text":"Hello",
            "number":a,
            "bin":b
        }
    }
    return render(request, "homepage.html",data)

def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password==confirm_password:

            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                email=email,
                password=password
            )

            return home(request)
        else:
            return render(request,"register.html")
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method=="POST":
        current_user_name=request.POST.get("user_name")
        current_password=request.POST.get("password")
        x=User.objects.all().get(user_name=current_user_name)
        if x:
            if x.password==current_password:
                return render(request,"homepage.html")
        print(x)
    else:
        return render(request,"loginpage.html")

question()

