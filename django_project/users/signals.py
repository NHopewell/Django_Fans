# a signal that gets fired when an object is saved (user model as sender)
from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
Create a new profile for each user.
post_save sends signal from User (sender)
to reciever (django.dispatch)
"""

def create_profile(sender, profile, created, **kwargs):
    pass