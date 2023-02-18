from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    review = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
