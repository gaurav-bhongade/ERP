# forms.py
from django import forms

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email")
    security_question = forms.CharField(label="Security Question")
    security_answer = forms.CharField(label="Security Answer", widget=forms.PasswordInput)


        



