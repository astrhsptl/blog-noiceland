from django.urls import path

from .views import add_like, get_post_likes, add_subscriber

urlpatterns = [
    path('likes/add/', add_like),
    path('likes/counts/', get_post_likes),
    path('subscribers/add/', add_subscriber),
]
