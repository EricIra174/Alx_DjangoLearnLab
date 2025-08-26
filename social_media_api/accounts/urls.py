from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView, FeedView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow_user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow_user"),
]
