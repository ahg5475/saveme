from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth



def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'account/signup.html')
    return render(request, 'account/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'account/login.html', {'error': '아이디나 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
