from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomSupplierUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomSupplierUser
        fields = ['email', 'name', 'address', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None 

# supplier/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# supplier/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomSupplierAuthenticationForm(AuthenticationForm):
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


