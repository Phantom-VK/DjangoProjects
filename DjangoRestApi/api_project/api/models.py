from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()
    cover_url = models.URLField(blank=True)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.title