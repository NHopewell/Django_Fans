from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User profile with profile pic
class Profile(models.Model):
    # one to one relationship with the user mode
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # save pics in this dir, extends MEDIA_DIR in settings.py
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') 

    def __str__(self):
        return f"{self.user.username} Profile"