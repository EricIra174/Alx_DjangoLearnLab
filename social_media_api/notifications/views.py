from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer, LikeNotificationSerializer, LikeNotificationDetailSerializer, UnLikeNotificationDetailSerializer
from posts.models import Like, Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework import generics, get_object_or_404
from django.contrib.auth.permissions import IsAuthenticated, permissions
from rest_framework.response import Response, status

# Create your views here.
        
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('-timestamp')
    
class CommentNotificationView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)
class PostNotificationView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)