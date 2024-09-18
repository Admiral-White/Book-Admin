from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book, AdminUser, AdminBorrowing
from .rabbitmq import publish_message
from .serializers import BookSerializer, AdminUserSerializer, AdminBorrowingSerializer


# List all books
class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Add a new book
class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        book = serializer.save()

        # Send message to RabbitMQ when a book is added
        message_body = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'publisher': book.publisher,
            'category': book.category,
        }
        publish_message(message_body)


# Remove a book
class DeleteBookView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'  # Delete by book ID


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

class AdminBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def unavailable_books(self, request):
        books = Book.objects.filter(is_available=False)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

class AdminBorrowingViewSet(viewsets.ModelViewSet):
    queryset = AdminBorrowing.objects.all()
    serializer_class = AdminBorrowingSerializer

    @action(detail=False, methods=['get'])
    def borrowed_books(self, request):
        borrowings = AdminBorrowing.objects.select_related('user', 'book')
        serializer = self.get_serializer(borrowings, many=True)
        return Response(serializer.data)
