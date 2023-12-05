from django.db import models
from datetime import datetime

class Posts(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=150000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)