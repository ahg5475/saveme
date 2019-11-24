from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from .forms import SignupForm

def signup(request):
    if request.method == "GET":
        return render(request, 'account/signup.html', {'f':SignupForm()})
    elif request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                new_user=User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                return HttpResponseRedirect(reverse('accounts:sucecce'))
            else:
                return render(request, 'account/signup.html', {'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})
        else:
             return render(request, 'account/signup.html',{'f':form})


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

def sucecce(request):
    return render(request, 'account/sucecce.html')

def id_overlap_check(request):
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        user = User.objects.get(username=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)
