from django.urls import path
from .views import (
    LikePostNotificationView,
    UnLikePostNotificationDetailView,
    NotificationListView,
    CommentNotificationView,
    PostNotificationView
)
urlpatterns = [
    path("notifications/", NotificationListView.as_view(), name="notification-list"),
    path("notifications/comments/", CommentNotificationView.as_view(), name="comment-notification"),
    path("notifications/posts/", PostNotificationView.as_view(), name="post-notification"),
]