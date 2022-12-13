"""Glass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexView.as_view(), name='home'),
    path('feedback', views.feedbackView.as_view(), name='feedback'),
    path('signUp', views.signUpView.as_view(), name='signup'),
    path('signin', views.signInView.as_view(), name='signin'),
    path('about', views.aboutView.as_view(), name='about'),
    path('', include('django.contrib.auth.urls')),
    path('record', views.recordView.as_view(), name='record'),
    path('account', views.accountView.as_view(), name='account')
]
