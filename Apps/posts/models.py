from django.db import models
from ..categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200,unique=True)
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    category = models.ManyToManyField(Category, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
