# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
       path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
     path("admin-page", views.admin_view, name="admin_view"),
    path("librarian-page/", views.librarian_view, name="librarian_view"),
    path("member-page/", views.member_view, name="member_view"),
     path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]
