from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    twitter_handle = models.URLField(max_length=50, blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'authors'
        ordering = ['author_name']
        indexes = [
            models.Index(fields=['author_name']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.author_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    LEVEL_CHOICES = [
            ('BGN', 'Beginner'),
            ('INT', 'Intermediate'),
            ('ADV', 'Advanced'),
        ]

    authors = models.ManyToManyField(Author, related_name='books')
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    #tech -specfic fields
    difficulty = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='BGN')
    categories = models.ManyToManyField(Category,related_name='books')
    # Media and Metadata
    cover_image = models.ImageField(upload_to='book_covers/',)
    book_url = models.URLField(blank=True)
    publisher = models.CharField(max_length=100,blank=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ='Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.authors}"

