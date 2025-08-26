# CRUD Operations

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)
book = Book.objects.get(title="1984")
print(book.id, book.title, book.author, book.publication_year)
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.id, book.title)
book = Book.objects.get(id=1)
book.delete()
print(Book.objects.all())
```
