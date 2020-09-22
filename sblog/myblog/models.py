from django.db import models
from django.urls import reverse
from datetime import datetime, date

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-publication_date", "-id"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("post-detail", args=str(self.id))
        return reverse("home")
