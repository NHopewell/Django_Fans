from django.urls import path
# views from views.py
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    # home route (blog/)
    path('', PostListView.as_view(), name="blog-home"),
    # posts for particular user
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    # post detail route, pk = primary key
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    # post create route
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    # post update route, pk = primary key
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    # post delete route, pk = primary key
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    # about route (blog/about/)
    path('about/', views.about, name="blog-about"),
]