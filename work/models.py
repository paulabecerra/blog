from django.db import models
from django.utils import timezone

#Work models.

class Work(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=True, null=True)
    finish_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.position
