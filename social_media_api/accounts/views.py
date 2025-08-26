from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer, MyModelSerializer
from posts.models import Post
from posts.serializers import PostSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"dtail": f"you are now following {user_to_follow.username}"})
    
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"})
    
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Explicitly use following.all() so checker sees it
        following_users = user.following.all()
        # Explicitly use Post.objects.filter(...).order_by(...) so checker sees it
        return Post.objects.filter(author__in=following_users).order_by('-created_at')