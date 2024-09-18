from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    return_date = models.DateField(null=True, blank=True)
    #available_from = models.DateField(null=True, blank=True)  # When it will be available if borrowed

    def __str__(self):
        return self.title


class AdminUser(models.Model):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class AdminBorrowing(models.Model):
    user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()


