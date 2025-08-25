from rest_framework import serializers
from .models import Notification
from posts.models import Like

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp']
class LikeNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
class LikeNotificationDetailSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at', 'post_title', 'user_username']
        read_only_fields = ['id', 'created_at', 'post_title', 'user_username']
        
class UnLikeNotificationDetailSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at', 'post_title', 'user_username']
        read_only_fields = ['id', 'created_at', 'post_title', 'user_username']