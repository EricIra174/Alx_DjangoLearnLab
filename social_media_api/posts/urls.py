from django.urls import path
from notifications.views import (
    LikePostNotificationView,
    UnLikePostNotificationDetailView,
)
from .views import PostViewSet, PostDetailView, CommentViewSet, CommentDetailView, FeedView
urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list'}), name='post-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentViewSet.as_view({'get': 'list'}), name='comment-list'),
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostNotificationView.as_view(), name='like-post-notification'),
    path('posts/<int:pk>/unlike/', UnLikePostNotificationDetailView.as_view(), name='unlike-post-notification'),
]