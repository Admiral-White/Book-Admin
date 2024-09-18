from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from catalogue.models import Book


class AddBookViewTest(APITestCase):

    def test_add_book(self):
        """Test adding a book via the API"""
        url = reverse('add-book')
        data = {
            "title": "Refactoring",
            "author": "Martin Fowler",
            "publisher": "Addison-Wesley",
            "category": "Technology",
            "is_available": True,
            "return_date": None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Refactoring')


class ListBooksViewTest(APITestCase):

    def setUp(self):
        Book.objects.create(
            title="Refactoring",
            author="Martin Fowler",
            publisher="Addison-Wesley",
            category="Technology",
            is_available=True,
            return_date=None
        )
        Book.objects.create(
            title="Design Patterns",
            author="Erich Gamma",
            publisher="Addison-Wesley",
            category="Technology",
            is_available=True,
            return_date=None
        )

    def test_list_books(self):
        """Test listing all books via the API"""
        url = reverse('list-books')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

