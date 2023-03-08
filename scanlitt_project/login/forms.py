from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import UserProfile

#define form classe for collecting data of users. 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'password_confirm', 'db_choices']
        widgets = {'password': forms.PasswordInput(), 'password_confirm': forms.PasswordInput()}

