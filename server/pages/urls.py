from django.urls import path, re_path, reverse_lazy

from .views import (
    HomeTemplateView, 
    CategoryListView,
    PostDeleteView, PostDetailView,
    PostListView, PostUpdateView,
    PostCreateView, 
)

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),

    path('categories/', CategoryListView.as_view(), name='category_list'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<uuid:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<uuid:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
