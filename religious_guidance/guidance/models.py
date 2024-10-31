from django.db import models
from user.models import UserProfile

class Religion(models.TextChoices):
    Buddhism = 'B', 'Buddhism'
    Christianity = 'C', 'Christianity'

# Create your models here.
class Guidance(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="guidance_images/")
    religion = models.CharField(max_length=1, choices=Religion.choices)
    favorite_users = models.ManyToManyField(UserProfile, related_name="favorite_guidances")

    def __str__(self) -> str:
        return f"{self.title} - {self.content}"