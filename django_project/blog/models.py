from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """
    Post model for new user posts.
    One to many relationship from user to post
    """
    # each attribte is a field in the db
    title = models.CharField(max_length=100) # character field with max len = 100 chars
    content = models.TextField() # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user deleted in User table, delete all their comments

    def __str__(self):
        return self.title

    # reverse returns full url to the route as a string, let view handle redirect
    def get_absolute_url(self):
        """
        Return path to a specific post, used for redirecting
        to specific post after use submits new post

        self.pk = primary key for a specific post
        post-detail url expects <int: pk>
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    """
    Comment model for commenting on posts.
    """
    post = models.ForeignKey('blog.Post', 
        on_delete=models.CASCADE, 
        related_name='comments')
    content = models.TextField() # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    # reverse returns full url to the route as a string, let view handle redirect
    def get_absolute_url(self):
        """
        Return path to a specific post, used for redirecting
        to specific post after use submits new post

        self.pk = primary key for a specific post
        post-detail url expects <int: pk>
        """
        return reverse('post-detail', kwargs={'pk': self.pk})