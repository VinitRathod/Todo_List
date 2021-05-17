from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()
    time = models.TimeField(auto_now=True)
    done = models.BooleanField(default=False)
