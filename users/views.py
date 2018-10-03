from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def user_login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()

    return render(request, 'account/user_login.html', {'form': form,
                                                       'menu_type': 1})


def user_register(request):
    if request.method == 'POST':
        pass
    else:
        form = RegisterForm()

    return render(request, 'account/user_register.html', {'form': form,
                                                          'menu_type': 2})