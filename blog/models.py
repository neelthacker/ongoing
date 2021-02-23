from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import django
from datetime import datetime
#from django.utils.text import slugify 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    created_on = models.DateTimeField(editable=True, auto_now_add=False, default=django.utils.timezone.now())
    slug = models.CharField(max_length=200, unique=True,)


    class Meta:
        ordering = ['-created_on']


    def get_absolute_url(self):
            return reverse('blog:home')

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.id)
    #     super(id, self).save(*args, **kwargs)
