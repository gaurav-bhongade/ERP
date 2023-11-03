# supplier/backends.py
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import CustomSupplierUser
from registration.models import CustomUser

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        if username is not None:
            # Try to authenticate with CustomUser model
            user = CustomUser.objects.filter(
                Q(email=username) | Q(contact=username)
            ).first()

            if user is not None and user.check_password(password):
                return user

        if email is not None:
            # Try to authenticate with CustomSupplierUser model
            user = CustomSupplierUser.objects.filter(email=email).first()

            if user is not None and user.check_password(password):
                return user

        return None

    def get_user(self, user_id):
        try:
            # Try to get the user from CustomUser model
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            try:
                # Try to get the user from CustomSupplierUser model
                return CustomSupplierUser.objects.get(pk=user_id)
            except CustomSupplierUser.DoesNotExist:
                return None
