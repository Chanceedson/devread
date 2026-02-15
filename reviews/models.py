from django.db import models
from books.models import Book
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Technical Review Data
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="1 to 5 stars"
    )
    # Specifics for tech context
    is_recommended = models.BooleanField(default=True)
    tech_stack_used = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g., 'Used this to learn Typescript'"
        )
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='reviews')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # A user shouldn't review the same book twice
        unique_together = ('book', 'user')
        ordering = ['-created_at']

        def __str__(self):
            return f"{self.rating}★ - {self.book.title} by {self.user.username}"

