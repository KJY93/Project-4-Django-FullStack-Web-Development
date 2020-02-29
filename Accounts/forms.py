from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.", label="Email address")
    firstname = forms.CharField(required=True, max_length=150, help_text="Required. 150 characters or fewer.", label="First name")
    lastname = forms.CharField(required=True, max_length=150, help_text="Required. 150 characters or fewer.", label="Last name")
    
    # 290220
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True, help_text="Required. Your at least 8 characters long password cannot be entirely numeric, cannot be a too commonly used password and cannot be too similar to your personal information.")
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput, required=True, help_text="Enter the same password as before, for verification.")

    class Meta:
        model = NewUser
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']
        
    def clean_email(self):
        User = get_user_model()
        user_email = self.cleaned_data.get('email')
        
        # check if email is unique using Django ORM
        if User.objects.filter(email=user_email):
            raise forms.ValidationError('The email address is already in use.')
        return user_email
        
    
# 160220 1137PM

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.", label="Email address")
    
    class Meta:
        model = NewUser
        fields = ['username', 'email', 'first_name', 'last_name']