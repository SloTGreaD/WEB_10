from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    
class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=50, default=None, null=True)    #ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)