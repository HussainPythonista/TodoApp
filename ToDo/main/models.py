from django.db import models

# Create your models here.
class toDo(models.Model):
    text=models.CharField(max_length=200)
    date_entered=models.DateTimeField()