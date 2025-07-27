from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def book_list(request):
    """
    Secure view to list books with search capability.
    - Uses Django forms to validate input (prevents SQL injection).
    - Uses ORM filters (safe query construction).
    """
    form = BookSearchForm(request.GET)
    books = Book.objects.all()
    if form.is_valid():
        query = form.cleaned_data['search_query']
        books = books.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

