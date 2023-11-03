# supplier/views.py

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

def home_supplier(request):
    return render(request, 'home_supplier.html')

def signup_supplier(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_supplier')
    else:
        form = SignUpForm()

    return render(request, 'signup_supplier.html', {'form': form})

# supplier/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomSupplierAuthenticationForm

def login_supplier(request):
    if request.method == 'POST':
        form = CustomSupplierAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirect to the desired page after login
            return redirect('home_supplier')  # Change 'dashboard' to the actual URL name
    else:
        form = CustomSupplierAuthenticationForm()

    return render(request, 'login_supplier.html', {'form': form})


def user_logout_supplier(request):
    logout(request)
    return redirect('login_supplier')
