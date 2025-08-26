from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, filters, viewsets
from .models import Post, Comment
from rest_framework import permissions, status
from rest_framework.response import Response
from notifications.models import Notification
from notifications.serializers import LikeNotificationSerializer, UnLikeNotificationDetailSerializer
from posts.models import Like
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionError("You do not have permission to delete this post.")
        instance.delete()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionError("You do not have permission to delete this comment.")
        instance.delete()

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                user=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        return Response({"message": "You already liked this post."}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"message": "You haven’t liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')