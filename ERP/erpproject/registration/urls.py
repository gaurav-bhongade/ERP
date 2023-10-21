from django.urls import path
from registration import views
from django.urls import path
from . import views

urlpatterns = [

    path('',views.Home_page,name='home_page'),
    path('signup/',views.SignupPage,name='signup'),

    path('home/',views.index,name='index'),
    path('logout/',views.LogoutPage,name='logout'),
    path('user-list/', views.get_all_users, name='user_list'),

    path('login/', views.login_view, name='login'),

    path('get_all_users/', views.get_all_users, name='get_all_users'),

     path('forgot-password/', views.ForgotPasswordPage, name='forgot_password'),

     path('edit_profile/', views.edit_profile_view, name='edit_profile'),
   
]

    
    
