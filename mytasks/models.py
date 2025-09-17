from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_details = models.TextField()
    task_date = models.DateTimeField()
    task_is_complete = models.BooleanField(default=False)
    task_priority = models.IntegerField(default=0)
    task_location = models.CharField(max_length=100)
    task_set_reminder = models.BooleanField(default=False)