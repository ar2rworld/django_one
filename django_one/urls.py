"""django_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django_one import views
from books import views as book_views
from django.conf import settings
from django.conf.urls.static import static
#import django_one.settings
#from django_one.views import trendingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView ),
    #path('trending/', trendingView ),
    path('time/', views.time),
    path('publishers/', views.publishersView),
    path('search/', book_views.search),
    path('stats/', views.stats),
    path('contact/', book_views.contact),
    path('contact/thanks/', book_views.thanks),
    path('add_publisher/thanks/', book_views.thanks),
    path('add_publisher/', book_views.add_publisher),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
