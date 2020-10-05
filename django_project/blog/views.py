from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment

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
    paginate_by = 4 # paginate home page 8 posts per

class UserPostListView(ListView):
    """
    User posts route: blog/user_posts.html
    ListView: contains list of Post objects for that user
    """
    model = Post
    template_name = 'blog/user_post.html' 
    context_object_name = 'posts'
    paginate_by = 4

    def get_queset(self):
        """
        Override to change what the ListView renders
        """
        # get user obj from db if exists, else return 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        # filter posts by user, order by date ascending
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    """
    Post Detail route: blog/post_detail.html route
    """
    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Post create route: blog/post_create.html route
    """
    model = Post
    fields = ['title', 'content']
    
    # override form_valid to add author before form is submitted
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Post create route: blog/post_create.html route
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """ 
        override form_valid to add author before form is submitted
        """
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        """
        UserPassesTestMixin method to validate current
        before attempting to update a post
        """
        # get current post
        post = self.get_object()
        # ensure current user is post author
        return True if self.request.user == post.author else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Post Detail route: blog/post_detail.html route
    """
    model = Post
    success_url = "/"

    def test_func(self):
        """
        UserPassesTestMixin method to validate current
        before attempting to update a post
        """
        # get current post
        post = self.get_object()
        # ensure current user is post author
        return True if self.request.user == post.author else False
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Post create route: blog/post_create.html route
    """
    model = Comment
    fields = ['content']
    
    # override form_valid to add author before form is submitted
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get("id"))
        form.instance.author = self.request.user

        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Post create route: blog/post_create.html route
    """
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        """ 
        override form_valid to add author before form is submitted
        """
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        """
        UserPassesTestMixin method to validate current
        before attempting to update a post
        """
        # get current post
        comment = self.get_object()
        # ensure current user is post author
        return True if self.request.user == comment.author else False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Post Detail route: blog/post_detail.html route
    """
    model = Comment
    success_url = "/"

    def test_func(self):
        """
        UserPassesTestMixin method to validate current
        before attempting to update a post
        """
        # get current post
        comment = self.get_object()
        # ensure current user is post author
        return True if self.request.user == comment.author else False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
