from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
