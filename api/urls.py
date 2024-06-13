from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserHomeView.as_view(), name='user-home'),
    path('user/<int:pk>/', userDetailsView.as_view(), name='user-details'),
    
    path('user/create-post/', CreatePostView.as_view(), name='create-post'),
    path('user/posts/<int:pk>/', RetrieveDestroyPostView.as_view(), name='retrieve-update-destroy-post'),
    path('user/posts/', ListAllPosts.as_view(), name='list-all-posts'),
]
