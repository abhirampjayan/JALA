from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    def __str__(self):
        return self.title
    