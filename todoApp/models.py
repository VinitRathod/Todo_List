from django.db import models
from django.utils import timezone

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now())
    done = models.BooleanField(default=False)
