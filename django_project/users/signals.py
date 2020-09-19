# a signal that gets fired when an object is saved (user model as sender)
from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
Create a new profile for each user.
post_save sends signal from User (sender)
to reciever (django.dispatch)
Receiver is a function that gets the signal
and performs some task
"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    receiver function that runs every time a user is created.
    signal = post_save
    sender = User
    instance = user instance
    created = was the user created?
    """
    # if that user was created, create a profile for that user
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    receiver function that runs every time a user is saved.
    """
    instance.profile.save()

