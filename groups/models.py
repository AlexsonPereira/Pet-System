from django.db import models

# Create your models here.
class Groups(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField()
