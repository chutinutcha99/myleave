"""leavesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import auth
from django.urls import include, path
from django.contrib.auth import views as authviews
from leaveapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('templates/', views.myIndex),
    #path('', views.myIndex, name='myIndex'),
    path('', views.dashboard, name='dashboard'),
    path('layout/', views.layout, name='layout'),
    path('approved/', views.approved, name='approved'),
    path('w_a_approved/', views.w_a_approved, name='w_a_approved'),
    path('disapproved/', views.disapproved, name='disapproved'),
    path('stats/', views.stats, name='stats'),
    
    path('members/', views.members, name='members'),
    #path('loginForm/', views.loginForm, name='loginForm'),
    path('login/', authviews.LoginView.as_view(), name='login'),
    path('logout/', authviews.LogoutView.as_view(), name='logout'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('signupForm/', views.signupForm, name='signupForm'),
    path('signup/', views.signup, name='signup'),
    path('signupForm/signup', views.signup, name='signupForm_signup'),
    path('leave_form', views.leave_form, name='leave_form'),
    path('approved_report/', views.approved_report, name='approved_report'),
    path('w_a_approved_report/', views.w_a_approved_report, name='w_a_approved_report'),
    path('disapproved_report/', views.disapproved_report, name='disapproved_report'),
    path('members_setting/', views.members_setting, name='members_setting'),
    path('sort_setting/', views.sort_setting, name='sort_setting'),
    path('department_setting/', views.department_setting, name='department_setting'),
    path('sort_edit/', views.sort_edit, name='sort_edit'),
   
    
    path('profile/', views.profile, name='profile'),
    #path('add/', views.add)
    

    

      
]