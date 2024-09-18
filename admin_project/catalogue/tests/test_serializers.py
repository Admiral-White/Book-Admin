from django.test import TestCase
from catalogue.models import Book
from catalogue.serializers import BookSerializer


class BookSerializerTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Clean Code",
            author="Robert Martin",
            publisher="Prentice Hall",
            category="Technology",
            is_available=True,
            return_date=None
        )

    def test_book_serializer(self):
        """Test if the serializer works correctly"""
        serializer = BookSerializer(self.book)
        data = serializer.data
        self.assertEqual(data['title'], "Clean Code")
        self.assertEqual(data['author'], "Robert Martin")
        self.assertEqual(data['publisher'], "Prentice Hall")
        self.assertEqual(data['category'], "Technology")
        self.assertEqual(data['is_available'], True)
        self.assertEqual(data['return_date'], None)
