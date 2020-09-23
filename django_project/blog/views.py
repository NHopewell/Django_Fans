from django.shortcuts import render # looks in templates folder
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    """
    Home route: blog/home.html
    ListView: contains list of Post objects
    """
    model = Post
    template_name = 'blog/home.html' #Default convention: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order posts ascending

class PostDetailView(DetailView):
    """
    Post Detail route: blog/post_detail.html route
    """
    model = Post
    context_object_name = 'post'

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
