from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def training(request):
    return render(request, 'training/t_index.html')

def calculator(request):
    return render(request, 'Calculator/bmi.html')

def notice(request):
    return render(request, 'notice/comunity.html')