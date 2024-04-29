from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_page'),
    path('kategori/',kategori, name='category_page'),
    path('detay/', detay, name='detail_page'),
    path('bagis/', bagis,name='donate_page'),
    path('kayit/', kayit, name='register_page'), 
    path('giris/', giris, name='login_page'),  
    path('sifre_degistir/', hesap, name='change-password_page'),
]
