# Create Book

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Expected Output:
# A new Book instance is created in the database.
# Printing the book:
print(book)
# Output:
# Book object (1)
```
