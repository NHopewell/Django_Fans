from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# User profile with profile pic
class Profile(models.Model):
    # one to one relationship with the user mode
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # save pics in this dir, extends MEDIA_DIR in settings.py
    image = models.ImageField(default='default.png', upload_to='profile_pics') 

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        """override save() to resize img to save
           room on file system"""
        super().save(*args, **kwargs)

        # resive img if largerß
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img = img.convert("RGB")
            img.save(self.image.path) # save to same path
