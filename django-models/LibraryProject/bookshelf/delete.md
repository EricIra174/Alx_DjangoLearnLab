# Delete Book

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
print(Book.objects.all())

# Expected Output:
# <QuerySet []>
```
