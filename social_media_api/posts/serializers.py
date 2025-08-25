from .models import Post, Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields =['title', 'content']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='Post')
    class Meta:
        model = Comment
        fields = ['content', 'author', 'post']
    def create(self, validated_data):
        post = validated_data.pop('Post')
        comment = Comment.objects.create(Post=post, **validated_data)
        return comment