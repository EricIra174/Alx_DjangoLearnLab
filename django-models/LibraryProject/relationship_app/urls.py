from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views module directly

urlpatterns = [
    # Book-related views
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    
    # Library detail view (class-based or function-based)
    path('library/<int:pk>/', views.library_detail, name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # User registration view (assumed to exist in views.py)
    path('register/', views.register, name='register'),
]
