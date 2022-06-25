from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = TaggableManager()
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "uploads/")
