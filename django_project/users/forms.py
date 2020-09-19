from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# 
class UserRegisterForm(UserCreationForm):
    """
    create user registration form which inherits 
    from UserCreationForm and adds an email field.
    """
    # specify additional feilds to add to form
    email = forms.EmailField(required=True)
    
    class Meta:
        # specify model we want this form to interact with 
        # (when we form.save(), save to this model)
        model = User
        # fields we want to show on form (in order):
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """
    Model form to update our user model,
    required before user can update her/his
    profile on the front end.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # allow user to update their username and email
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    Model form to allow user to update their
    profile (with a new profile pic)
    """
    class Meta:
        model = Profile
        fields = ['image']