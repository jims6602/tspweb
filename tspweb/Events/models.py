from django.db import models

class Event(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.TextField()
