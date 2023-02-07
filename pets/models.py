from django.db import models

# Create your models here.
class SexPets(models.TextChoices):
    FEMALE = "female"
    MALE = "male"
    NOTINFORMED = "not informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=SexPets.choices, default=SexPets.NOTINFORMED
    )
