from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    kategoriler = Category.objects.all()
    context = {'kategoriler':kategoriler}
    return render(request,'index.html', context)


def kategori(request):
    kategoriler = Category.objects.all()
    context = {'kategoriler':kategoriler}
    return render(request,'category.html', context)

def detay(request):
    kategoriler = Category.objects.all()
    haber = get_object_or_404(Haber)
    context = {'kategoriler':kategoriler,
    'haber':haber}
    return render(request,'detail-page.html', context)
    
def bagis(request):
    context = {}
    return render(request,'donation.html', context)

def kayit(request):
    context = {}
    return render(request,'register.html', context)
    """
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def kayit(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index_page')
            
    else:
        form = UserCreationForm()
        
    return render(request, 'kayit.html', {
        'form': form
        })
    """

def giris(request):
    context = {}
    return render(request,'login.html', context)
    """
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login

def giris(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index_page')
            
    return render(request, 'giris.html')
    """

def hesap(request):
    pass
    """
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def sifre_degistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Şifre değiştirildi.')
            return redirect('index_page')   
        else:
            messages.error(request, 'Lütfen doğru bilgileri giriniz.')
            
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'sifre_degistir.html', {
        'form': form
        })
    """