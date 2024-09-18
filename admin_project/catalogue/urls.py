from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import ListBooksView, AddBookView, DeleteBookView, AdminBookViewSet, AdminBorrowingViewSet, AdminUserViewSet

router = DefaultRouter()
router.register('adminusers', AdminUserViewSet)
router.register('books', AdminBookViewSet)
router.register('borrowings', AdminBorrowingViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library Admin API",
        default_version='v1',
        description="API documentation for the library Admin service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@library.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('books/add/', AddBookView.as_view(), name='add-book'),
    path('books/<int:id>/delete/', DeleteBookView.as_view(), name='delete-book'),
    path('unavailable_books/', AdminBookViewSet.unavailable_books, name='unavailable_books'),
    path('borrowed_books/', AdminBorrowingViewSet.borrowed_books, name='borrowed_books'),
    path('', include(router.urls)),
]
