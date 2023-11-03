from django.urls import path
from .views import signup_supplier, login_supplier, user_logout_supplier,home_supplier

urlpatterns = [
    path('home_supplier/', home_supplier, name='home_supplier'),
    path('signup_supplier/', signup_supplier, name='signup_supplier'),
    path('login_supplier/', login_supplier, name='login_supplier'),
    path('logout_supplier/', user_logout_supplier, name='logout_supplier'),
]