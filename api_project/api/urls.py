from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books', BookList)
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api/', include(router.urls)),
    path('books/', BookList.as_view({'get': 'list'}), name='book-list'),
    path('admin/', admin.site.urls),
    path('', include('router.urls')),  
]

