from django.urls import path
from .views import AuthorListCreateAPIView, AuthorDetailAPIView, PublisherListCreateAPIView, PublisherDetailAPIView, \
    BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('publishers/', PublisherListCreateAPIView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>/', PublisherDetailAPIView.as_view(), name='publisher-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
