from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

