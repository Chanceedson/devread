from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500,blank=True)
    github_username = models.CharField(max_length=100,blank=True)
    website = models.URLField(max_length=100,blank=True)
    primary_techstack = models.CharField(max_length=100, help_text='eg. Python/Django')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        indexes = [
            models.Index(fields = ['primary_techstack'])
        ]

    def __str__(self) -> str:
        return self.email
