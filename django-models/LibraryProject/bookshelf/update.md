# Update Book

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.id, book.title)

# Expected Output:
# 1 Nineteen Eighty-Four
```
