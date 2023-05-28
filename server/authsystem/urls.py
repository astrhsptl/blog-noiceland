from django.urls import path, include

from .views import UserUpdateView, AuthorsListView, AuthorDetail

urlpatterns = [
    path('', include('allauth.urls')),

    path('me/update/<uuid:pk>', UserUpdateView.as_view(), name='me_update'),

    path('authors/', AuthorsListView.as_view()),
    path('author/<uuid:pk>', AuthorDetail.as_view(), name='user_detail')
]

