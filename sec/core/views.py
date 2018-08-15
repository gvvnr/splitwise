from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from forms import SignUpForm



def auth_login(request, user):
    pass


def profile(request):
    return render(request,'profile.html')

def signup(request):
    print("dfgvfdsdvgfds")
    if request.method == 'POST':
        print("0987654321234567")
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("23456789987654")
            user = form.save()
            auth_login(request, user)
            return redirect('homePage')
        else:
            print("form in valid")

    else:
        print("sdgfdsfdsxc")
        form = SignUpForm()
    return render(request, 'Signup.html', {'form': form})



def home(request):
    return render(request,'homePage.html')

