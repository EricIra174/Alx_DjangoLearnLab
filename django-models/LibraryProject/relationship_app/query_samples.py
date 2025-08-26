import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()
from relationship_app.models import Author, Book, Library, Librarian
# Querying all books by a specific author
def get_books_by_author(author_name):
    try:
        author=Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")
    
#list all books in a library
def get_all_books_in_library(library_name):
    try:
        library=Library.objects.get(library=library_name)
        books= library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# retreive the librarian for a library
def get_librarian_for_a_library(library_name):
    try:
        library= Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
if __name__ == "__main__":
    # Example usage
    get_books_by_author("John Doe")
    get_all_books_in_library("City Library")
    get_librarian_for_a_library("City Library")  # Assuming the library exists