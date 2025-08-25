from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, PostDetailView, PostListView, PostUpdateView, PostDeleteView, edit_profile, CommentDeleteView, CommentDetailView, CommentListView, CommentUpdateView, CommentCreateView
from . import views

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("profile/", TemplateView.as_view(template_name="blog/profile.html"), name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("post/new/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("comment/<int:pk>/", CommentDetailView.as_view(), name="comment_detail"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("comment/", CommentListView.as_view(), name="comment_list"),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="add_comment"),
    path("", views.post_list, name="post_list"),
    path("search/", views.search_posts, name="search_posts"),
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="posts_by_tag"),
]
