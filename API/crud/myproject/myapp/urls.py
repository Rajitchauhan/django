from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-detail'),
]
