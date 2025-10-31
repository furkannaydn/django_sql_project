# English: Import necessary functions from Django and views from the current app.
# Türkçe: Django'dan gerekli fonksiyonları ve mevcut uygulamadan view'ları içeri aktar.
from django.urls import path
from . import views

urlpatterns = [
    # English: Map the root URL of this app to the 'index' view.
    # When a user visits '/databaseapp/', this view will be triggered.
    # Türkçe: Bu uygulamanın kök URL'ini 'index' view'ına yönlendir.
    # Kullanıcı '/databaseapp/' adresini ziyaret ettiğinde bu view tetiklenir.
    path('', views.index, name='index'),
]