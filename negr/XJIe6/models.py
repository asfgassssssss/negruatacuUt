from django.db import models

# Create your models here.
from django.urls import reverse



class TheBestBooks(models.Model):
    BooksName = models.CharField(max_length=40)
    Author = models.CharField(max_length=15)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)
    DateOfBirth = models.CharField(max_length=10)
    Summary = models.TextField(blank=True)
    Cost = models.IntegerField(default=700)
    Interest = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('book',kwargs={'book_slug': self.slug})


    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'



