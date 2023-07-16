from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')
def adv_post(request):
    return render(request, 'advertisement-post.html')
def regist(request):
    return render(request, 'register.html')
def log_in(request):
    return render(request, 'login.html')
def pro_file(request):
    return render(request, 'profile.html')