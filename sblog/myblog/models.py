from django.db import models
from django.urls import reverse
from datetime import datetime, date

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


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
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="not categorized")
    likes = models.ManyToManyField(User, related_name="blog_post")
    snippets = models.CharField(max_length=255)

    class Meta:
        ordering = ["-publication_date", "-id"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("post-detail", args=str(self.id))
        return reverse("home")

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")


    def __str__(self):
        return "{} - {}".format(self.post.title, self.name)
