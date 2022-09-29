"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blog import views
 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='homepage'),
    path('about/', views.AboutPage, name='aboutpage'),
    path('dashboard/', views.DashboardPage, name='dashboardpage'),
    path('contact/', views.ContactPage, name='contactpage'),
    path('signup/', views.SignupPage, name='signuppage'),
    path('login/', views.LoginPage, name='loginpage'),
    path('logout/', views.LogoutPage, name='logoutpage'), 
    path('addpost/', views.AddPost, name='addpost'),  
    path('updatepost/<int:id>/', views.UpdatePost, name='updatepost'),  
    path('delpost/<int:id>/', views.Delpost, name='delpost'),  
]
