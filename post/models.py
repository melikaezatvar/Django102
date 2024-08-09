from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024, null=True)
    author = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
