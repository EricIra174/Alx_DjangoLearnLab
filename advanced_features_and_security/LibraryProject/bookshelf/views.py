# bookshelf/views.py

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
def book_search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
def form_example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
