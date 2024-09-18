from django.test import TestCase
from catalogue.models import Book


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="The Pragmatic Programmer",
            author="Andrew Hunt",
            publisher="Addison-Wesley",
            category="Technology",
            is_available=True,
            return_date=None
        )

    def test_book_creation(self):
        """Test if the book is created successfully"""
        self.assertEqual(self.book.title, "The Pragmatic Programmer")
        self.assertEqual(self.book.author, "Andrew Hunt")
        self.assertEqual(self.book.publisher, "Addison-Wesley")
        self.assertEqual(self.book.category, "Technology")
        self.assertEqual(self.book.is_available, True)
        self.assertEqual(self.book.return_date, None)

    def test_book_str(self):
        """Test string representation of the book"""
        self.assertEqual(str(self.book), "The Pragmatic Programmer")
