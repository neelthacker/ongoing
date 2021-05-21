from django.db import models
from django.contrib.auth.models import User
import django
# Create your models here.

class Feedback(models.Model):    
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbackAuther')
    created = models.DateTimeField(auto_now_add=True)
    permission = models.BooleanField(default=False)
