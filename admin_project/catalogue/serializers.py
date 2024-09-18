from rest_framework import serializers
from .models import Book, AdminBorrowing, AdminUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AdminBorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminBorrowing
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['id', 'email', 'firstname', 'lastname']
