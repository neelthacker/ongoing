from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import django
from datetime import datetime


def unique_slug():
    value = datetime.now().strftime("%S%f")
    return value
# Create your models here.


class Category(models.Model):
    """ This model is for Category """
    title = models.CharField(max_length=255, unique=True,
                             verbose_name="Title for category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    """ This model is for Post """
    title = models.CharField('title for post', max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(
        editable=True, auto_now_add=False, default=django.utils.timezone.now())
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('blog:home')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = unique_slug()
        super(Post, self).save(*args, **kwargs)
