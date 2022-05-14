from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.forms import LoginForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request.POST)
                messages.success(request, 'Bienvenue' + ' ' + request.user.username)
                return redirect('home')
            else:
                messages.warning(request, 'try again')
                return redirect('login')
        else:
            messages.error(request, 'form invalide')
            return redirect('login')
    else:
        form = LoginForm
        cx = {'form': form}
        return render(request, 'user/login.html', cx)

def user_logout(request):
    logout(request)
