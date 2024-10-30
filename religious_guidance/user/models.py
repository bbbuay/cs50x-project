from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"