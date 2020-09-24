from django.db import models
from django.urls import reverse
from datetime import datetime, date

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
    # return reverse("post-detail", args=str(self.id))
        return reverse("home")

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="not categorized")


    class Meta:
        ordering = ["-publication_date", "-id"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("post-detail", args=str(self.id))
        return reverse("home")
