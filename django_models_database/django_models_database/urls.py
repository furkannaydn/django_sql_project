"""
URL configuration for django_models_database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # English: URL path for the Django admin site.
    # Türkçe: Django yönetim sitesi için URL yolu.
    path('admin/', admin.site.urls),
    # English: Include URLs from the 'database_app' application for any path starting with 'databaseapp/'.
    # Türkçe: 'databaseapp/' ile başlayan tüm yollar için 'database_app' uygulamasının URL'lerini dahil et.
    path('databaseapp/', include('database_app.urls')),
]
