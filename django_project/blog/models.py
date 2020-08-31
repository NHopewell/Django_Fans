from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    # each attribte is a field in the db
    title = models.CharField(max_length=100) # character field with max len = 100 chars
    content = models.TextField() # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user deleted in User table, delete all their comments

    def __str__(self):
        return self.title