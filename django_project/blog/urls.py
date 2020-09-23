from django.urls import path
# views from views.py
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # home route (blog/)
    path('', PostListView.as_view(), name="blog-home"),
    # post detail route, pk = primary key
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    # about route (blog/about/)
    path('about/', views.about, name="blog-about"),
]