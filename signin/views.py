from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib import auth
from tasks import *

# Create your views here.
def index(request):       
    return render(request,'index.html')

def login_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user:
        auth.login(request, user)
    #    return HttpResponse("welcome! " + username)
        return redirect('list')
    else:
        return render(request,'index.html')

def logout_page(request):
    print('next_href', request.path)
    return render(request, 'logout.html')

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

