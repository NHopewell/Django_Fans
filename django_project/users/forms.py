from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# 
class UserRegisterForm(UserCreationForm):
    """
    create user registration form which inherits 
    from UserCreationForm and adds an email field.
    """

    email = forms.EmailField(required=True)
    
    class Meta:
        # specify model we want this form to interact with 
        # (when we form.save(), save to this model)
        model = User
        # fields we want to show on form (in order):
        fields = ['username', 'email', 'password1', 'password2']
