from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    # Book-related views
    path('add_book/', views.add_book, name="add_book"),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Library detail
    path('library/<int:pk>/', views.library_detail, name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
]
